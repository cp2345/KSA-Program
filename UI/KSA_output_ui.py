# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KSA_Output.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_outputDialog(object):
    def setupUi(self, outputDialog):
        outputDialog.setObjectName("outputDialog")
        outputDialog.resize(1067, 524)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        outputDialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(outputDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(outputDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.knowledgeTable = QtWidgets.QTableWidget(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.knowledgeTable.setFont(font)
        self.knowledgeTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.knowledgeTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.knowledgeTable.setObjectName("knowledgeTable")
        self.knowledgeTable.setColumnCount(2)
        self.knowledgeTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.knowledgeTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.knowledgeTable.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.knowledgeTable)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 2, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(outputDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.abilityTable = QtWidgets.QTableWidget(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.abilityTable.setFont(font)
        self.abilityTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.abilityTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.abilityTable.setObjectName("abilityTable")
        self.abilityTable.setColumnCount(2)
        self.abilityTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.abilityTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.abilityTable.setHorizontalHeaderItem(1, item)
        self.abilityTable.horizontalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_3.addWidget(self.abilityTable)
        self.gridLayout.addWidget(self.groupBox_3, 1, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(outputDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.skillsTable = QtWidgets.QTableWidget(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.skillsTable.setFont(font)
        self.skillsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.skillsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.skillsTable.setObjectName("skillsTable")
        self.skillsTable.setColumnCount(2)
        self.skillsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.skillsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.skillsTable.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.skillsTable)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 2, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(outputDialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MosChoiceLabel = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.MosChoiceLabel.setFont(font)
        self.MosChoiceLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MosChoiceLabel.setObjectName("MosChoiceLabel")
        self.horizontalLayout.addWidget(self.MosChoiceLabel)
        self.MOSDrop = QtWidgets.QComboBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.MOSDrop.setFont(font)
        self.MOSDrop.setObjectName("MOSDrop")
        self.horizontalLayout.addWidget(self.MOSDrop)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.retranslateUi(outputDialog)
        QtCore.QMetaObject.connectSlotsByName(outputDialog)

    def retranslateUi(self, outputDialog):
        _translate = QtCore.QCoreApplication.translate
        outputDialog.setWindowTitle(_translate("outputDialog", "Dialog"))
        self.groupBox.setTitle(_translate("outputDialog", "Knowledge"))
        item = self.knowledgeTable.horizontalHeaderItem(0)
        item.setText(_translate("outputDialog", "Attribute"))
        item = self.knowledgeTable.horizontalHeaderItem(1)
        item.setText(_translate("outputDialog", "Difference"))
        self.groupBox_3.setTitle(_translate("outputDialog", "Abilities"))
        item = self.abilityTable.horizontalHeaderItem(0)
        item.setText(_translate("outputDialog", "Attribute"))
        item = self.abilityTable.horizontalHeaderItem(1)
        item.setText(_translate("outputDialog", "Difference"))
        self.groupBox_2.setTitle(_translate("outputDialog", "Skills"))
        item = self.skillsTable.horizontalHeaderItem(0)
        item.setText(_translate("outputDialog", "Attribute"))
        item = self.skillsTable.horizontalHeaderItem(1)
        item.setText(_translate("outputDialog", "Difference"))
        self.groupBox_4.setTitle(_translate("outputDialog", "MOS Choice"))
        self.MosChoiceLabel.setText(_translate("outputDialog", "MOS:"))
        self.pushButton.setText(_translate("outputDialog", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    outputDialog = QtWidgets.QDialog()
    ui = Ui_outputDialog()
    ui.setupUi(outputDialog)
    outputDialog.show()
    sys.exit(app.exec_())
