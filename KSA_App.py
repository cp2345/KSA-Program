from PyQt5.QtWidgets import QDialog, QErrorMessage, QMainWindow, QTableWidgetItem, QApplication, QHeaderView
from PyQt5 import QtCore
from UI import KSA_main_ui, KSA_input_ui, KSA_output_ui, KSA_compare_ui, KSA_user_guide_ui
import sys
from src import CalculateDifferences, Calculator

ideal_knowledge_dict = {}
ideal_skill_dict = {}
ideal_ability_dict = {}
knowledge_averages = Calculator.knowledge_averages
skill_averages = Calculator.skill_averages
ability_averages = Calculator.ability_averages

# Creates a custom item that accepts float values for accurate sorting
class QCustomTableWidgetItem(QTableWidgetItem):
    def __init__(self, value):
        super(QCustomTableWidgetItem, self).__init__('%s' % value)

    def __lt__(self, other):
        if (isinstance(other, QCustomTableWidgetItem)):
            selfDataValue = float(str(self.data(QtCore.Qt.EditRole)))
            otherDataValue = float(str(other.data(QtCore.Qt.EditRole)))
            return selfDataValue < otherDataValue
        else:
            return QTableWidgetItem.__lt__(self, other)


class usersGuide(QDialog, KSA_user_guide_ui.Ui_Users_Guide):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        with open('resources/Users_Guide.html', 'r') as guide:
            self.textBrowser.insertHtml(guide.read())
        self.textBrowser.setOpenExternalLinks(True)


class compareWindow(QDialog, KSA_compare_ui.Ui_compareDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        global knowledge_averages
        global skill_averages
        global ability_averages
        global MOS_dropdown
        self.setWindowTitle("Comparison")
        self.Mos1Drop.addItems(MOS_dropdown)
        self.Mos2Drop.addItems(MOS_dropdown)
        self.CompareButton.clicked.connect(self.compare_all)

    def compare_all(self):
        self.compare(knowledge_averages, self.KnowledgeTable)
        self.compare(skill_averages, self.SkillTable)
        self.compare(ability_averages, self.AbilityTable)

    def compare(self, average_dict, table):
        mos1 = self.Mos1Drop.currentText()
        mos2 = self.Mos2Drop.currentText()
        self.make_table(average_dict[mos1], average_dict[mos2], table)

    def make_table(self, _dict1, _dict2, table):
        table.setSortingEnabled(0)
        table.setRowCount(0)
        row = 0
        for key in _dict1.keys():
            item = QTableWidgetItem(str(key))
            value1 = QCustomTableWidgetItem(_dict1[key])
            value2 = QCustomTableWidgetItem(_dict2[key])
            table.insertRow(row)
            table.setItem(row, 0, item)
            table.setItem(row, 1, value1)
            table.setItem(row, 2, value2)
            row += 1
        row_count = table.rowCount()
        for row in range(row_count):
            item1 = table.item(row, 1)
            value1 = float(QTableWidgetItem.text(item1))
            item2 = table.item(row, 2)
            value2 = float(QTableWidgetItem.text((item2)))
            value3 = round((value1 - value2), 1)
            item = QCustomTableWidgetItem(value3)
            table.setItem(row, 3, item)
        table.setSortingEnabled(1)
        table.sortItems(0, QtCore.Qt.AscendingOrder)
        self.change_table_headers(table)

    def change_table_headers(self, table):
        mos1 = QTableWidgetItem(f"MOS: {self.Mos1Drop.currentText()}")
        mos2 = QTableWidgetItem(f"MOS: {self.Mos2Drop.currentText()}")
        table.setHorizontalHeaderItem(1, mos1)
        table.setHorizontalHeaderItem(2, mos2)
        self.resize_headers_to_fit(table)

    def resize_headers_to_fit(self, table):
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)


class inputWindow(QDialog, KSA_input_ui.Ui_builderDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Build your Ideal Fit for the job")
        self.saveButton.clicked.connect(self.save_all_values)
        self.saveAndClose.clicked.connect(self.save_and_close)
        self.KnowledgeApply.clicked.connect(self.setKnowledgeDefault)
        self.SkillsApply.clicked.connect(self.setSkillDefault)
        self.AbilityApply.clicked.connect(self.setAbilityDefault)

    def setKnowledgeDefault(self):
        self.default_value_set(self.DefaultKnowledgeEntry, self.knowledgTable)

    def setSkillDefault(self):
        self.default_value_set(self.DefaultSkillEntry, self.skillsTable)

    def setAbilityDefault(self):
        self.default_value_set(self.DefaultAbilityEntry, self.abilityTable)

    def default_value_set(self, line_edit, table):
        row_count = table.rowCount()
        value = line_edit.text()
        try:
            float(value)
        except ValueError:
            self.invalid_default()
        else:
            if 0 <= float(value) <= 100:
                for row in range(row_count):
                    current_row = row -1
                    item = QTableWidgetItem(value)
                    table.setItem(current_row, 1, item)
            else:
                self.invalid_default()

    def save_all_values(self):
        global ideal_knowledge_dict
        global ideal_skill_dict
        global ideal_ability_dict
        ideal_knowledge_dict = {}
        ideal_skill_dict = {}
        ideal_ability_dict = {}
        rowCountK = self.knowledgTable.rowCount()
        rowCountS = self.skillsTable.rowCount()
        rowCountA = self.abilityTable.rowCount()

        for row in range(rowCountK):
            try:
                attribute = self.knowledgTable.verticalHeaderItem(row)
                attribute_str = str(attribute.text())
                item = self.knowledgTable.item(row, 0)
                item_float = float(item.text())

            except:
                break

            else:
                if 0 <= item_float <= 100:
                    ideal_knowledge_dict[attribute_str] = item_float

        for row in range(rowCountS):
            try:
                attribute = self.skillsTable.verticalHeaderItem(row)
                attribute_str = str(attribute.text())
                item = self.skillsTable.item(row, 0)
                item_float = float(item.text())

            except:
                break

            else:
                if 0 <= item_float <= 100:
                    ideal_skill_dict[attribute_str] = item_float

        for row in range(rowCountA):
            try:
                attribute = self.abilityTable.verticalHeaderItem(row)
                attribute_str = str(attribute.text())
                item = self.abilityTable.item(row, 0)
                item_float = float(item.text())

            except:
                break

            else:
                if 0 <= item_float <= 100:
                    ideal_ability_dict[attribute_str] = item_float
        while True:
            if len(ideal_knowledge_dict) != 33:
                self.invalid_entries_error()
                break
            if len(ideal_skill_dict) != 35:
                self.invalid_entries_error()
                break
            if len(ideal_ability_dict) != 52:
                self.invalid_entries_error()
                break
            break

    def save_and_close(self):
        self.save_all_values()
        if len(ideal_knowledge_dict) == 33:
            self.close()

    def invalid_entries_error(self):
        error_dialog = QErrorMessage()
        error_dialog.setWindowTitle('Error')
        error_dialog.showMessage('INVALID ENTRIES DETECTED! '
                                 'Please ensure that all values entered are between 0 and 100, and that '
                                 'all cells are filled out.')
        error_dialog.exec_()

    def invalid_default(self):
        error_dialog = QErrorMessage()
        error_dialog.setWindowTitle('Error')
        error_dialog.showMessage('INVALID ENTRY DETECTED! Please only enter values between 0 and 100')
        error_dialog.exec_()


class outputWindowSingle(QDialog, KSA_output_ui.Ui_outputDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        global knowledge_averages
        global skill_averages
        global ability_averages
        global MOS_dropdown
        self.setWindowTitle("View single MOS averages")
        self.MOSDrop.addItems(MOS_dropdown)
        self.set_header(self.knowledgeTable)
        self.set_header(self.skillsTable)
        self.set_header(self.abilityTable)
        self.pushButton.clicked.connect(self.generate_tables)
        self.pushButton.setText("View")

    def generate_tables(self):
        selected_mos = self.MOSDrop.currentText()
        self.make_table(knowledge_averages[selected_mos], self.knowledgeTable)
        self.make_table(skill_averages[selected_mos], self.skillsTable)
        self.make_table(ability_averages[selected_mos], self.abilityTable)
        self.setWindowTitle(f"Averages for MOS: {selected_mos}")

    def make_table(self, _dict, table):
        table.setRowCount(0)
        row = 0
        table.setSortingEnabled(0)
        for key in _dict:
            item = QTableWidgetItem(str(key))
            value = QCustomTableWidgetItem(_dict[key])
            table.insertRow(row)
            table.setItem(row, 0, item)
            table.setItem(row, 1, value)
            row += 1
        table.setSortingEnabled(1)
        table.sortItems(0, QtCore.Qt.AscendingOrder)
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

    def set_header(self, table):
        header = 'Value'
        item = QTableWidgetItem(header)
        table.setHorizontalHeaderItem(1, item)


class outputWindowDiff(QDialog, KSA_compare_ui.Ui_compareDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        global MOS_dropdown
        self.label.setText("MOS")
        self.label_2.setText("Ideal Fit")
        self.Mos1Drop.addItems(MOS_dropdown)
        self.Mos2Drop.addItem("Ideal Fit")
        self.CompareButton.clicked.connect(self.compare_all)

    def compare_all(self):
        self.compare(knowledge_averages, ideal_knowledge_dict, self.KnowledgeTable)
        self.compare(skill_averages, ideal_skill_dict, self.SkillTable)
        self.compare(ability_averages, ideal_ability_dict, self.AbilityTable)
        self.setWindowTitle(f"Comparison between MOS: {self.Mos1Drop.currentText()} and your ideal fit")

    def compare(self, average_dict, ideal_dict,  table):
        mos = self.Mos1Drop.currentText()
        self.make_table(average_dict[mos], ideal_dict, table)

    def make_table(self, _dict1, _dict2, table):
        table.setSortingEnabled(0)
        table.setRowCount(0)
        row = 0
        for key in _dict1.keys():
            item = QTableWidgetItem(str(key))
            value1 = QCustomTableWidgetItem(_dict1[key])
            value2 = QCustomTableWidgetItem(_dict2[key])
            table.insertRow(row)
            table.setItem(row, 0, item)
            table.setItem(row, 1, value1)
            table.setItem(row, 2, value2)
            row += 1
        row_count = table.rowCount()
        for row in range(row_count):
            item1 = table.item(row, 1)
            value1 = float(QTableWidgetItem.text(item1))
            item2 = table.item(row, 2)
            value2 = float(QTableWidgetItem.text((item2)))
            value3 = round((value1 - value2), 1)
            item = QCustomTableWidgetItem(str(value3))
            table.setItem(row, 3, item)
        table.setSortingEnabled(1)
        table.sortItems(0, QtCore.Qt.AscendingOrder)
        self.change_table_headers(table)

    def change_table_headers(self, table):
        mos = QTableWidgetItem(f"MOS: {self.Mos1Drop.currentText()}")
        ideal_fit = QTableWidgetItem("Ideal Fit")
        table.setHorizontalHeaderItem(1, mos)
        table.setHorizontalHeaderItem(2, ideal_fit)
        self.resize_headers_to_fit(table)

    def resize_headers_to_fit(self, table):
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)


class MainWindow(QMainWindow, KSA_main_ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        global knowledge_averages
        global skill_averages
        global ability_averages
        self.setWindowTitle("KSA Program")
        self.buildButton.clicked.connect(self.inputWindow)
        self.calculateTotal.clicked.connect(self.display_totals)
        self.MOSSelectButton.clicked.connect(self.outputWindowDiff)
        self.MOSSelectButton2.clicked.connect(self.outputWindowSingle)
        self.compareButton.clicked.connect(self.compareWindow)
        self.actionExit.triggered.connect(self.close_app)
        self.actionUsers_Guide.triggered.connect(self.display_user_guide)

    def close_app(self):
        sys.exit()

    def no_ideal_built_error(self):  # This will make an error saying that the ideal list isn't built yet
        error_dialog = QErrorMessage()
        error_dialog.setWindowTitle('Error')
        error_dialog.showMessage('Please build your ideal fit before calculating')
        error_dialog.exec_()

    def inputWindow(self):  # Makes the input window pop up
        self.w = inputWindow()
        self.w.show()

    def outputWindowDiff(self):
        global ideal_knowledge_dict
        if len(ideal_knowledge_dict) == 0:
            self.no_ideal_built_error()
        else:
            self.w = outputWindowDiff()
            self.w.show()

    def outputWindowSingle(self):
        self.w = outputWindowSingle()
        self.w.show()

    def compareWindow(self):
        self.w = compareWindow()
        self.w.show()

    def display_totals(self):
        self.totalMOSTable.setSortingEnabled(0)
        self.totalMOSTable.setRowCount(0)
        global ideal_knowledge_dict
        global ideal_skill_dict
        global ideal_ability_dict
        if len(ideal_knowledge_dict) == 0:
            self.no_ideal_built_error()
        else:
            totals = CalculateDifferences.calculateDifferences(knowledge_averages, ideal_knowledge_dict,
                                                               skill_averages, ideal_skill_dict,
                                                               ability_averages, ideal_ability_dict)
            # totals.knowledge, totals.skill, and totals.ability generated {MOS:{att:#,att:#,..}, MOS{}...}
            total = CalculateDifferences.addUpDifferences(totals.knowledge, totals.skill, totals.ability)
            # total.total_for_all_mos generated, and holds the grand totals {MOS:total, MOS:total, MOS:total...}
            row = 0
            for key in total.total_for_all_mos:
                item = QTableWidgetItem(str(key))
                value = total.total_for_all_mos[key]
                value_item = QCustomTableWidgetItem(value)
                self.totalMOSTable.insertRow(row)
                self.totalMOSTable.setItem(row, 0, item)
                self.totalMOSTable.setItem(row, 1, value_item)
                row += 1
            self.totalMOSTable.setSortingEnabled(1)
            self.totalMOSTable.sortItems(1, QtCore.Qt.DescendingOrder)

    def display_user_guide(self):
        self.w = usersGuide()
        self.w.show()
        self.w.textBrowser.verticalScrollBar().setValue(0)


class MOS_Dropdown_setup:
    def __init__(self, avg_dict):
        MOS_dropdown_list = []
        for i in avg_dict:
            MOS_dropdown_list.append(i)
        self.MOS_dropdown = sorted(MOS_dropdown_list)

MOS_dropdown = MOS_Dropdown_setup(knowledge_averages).MOS_dropdown

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
