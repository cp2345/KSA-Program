import csv


class MosDict:

    def __init__(self):
        self.mos_dict = {}

    def read_mos(self, filename):
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                _list = []
                for value in row[0:29]:
                    if not value == "":
                        _list.append(value)
                self.mos_dict[_list.pop(0)] = _list
            return self.mos_dict


class MakeSocKnowledgeDict:

    def __init__(self):
        self.knowledge_dict = {}

    def read_knowledge(self, filename):
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            _attribute_list = []
            for row in csvreader:
                _dict = {}
                _list = []
                for value in row:
                    _list.append(value)
                soc_code = _list[0]
                attribute = _list[1]
                number = _list[2]
                _dict[attribute] = number
                _attribute_list.append(_dict)
                if len(_attribute_list) == 33:
                    self.knowledge_dict[soc_code] = _attribute_list
                    _attribute_list = []
        for code in self.knowledge_dict:
            _temp_dict = {}
            for attribute in self.knowledge_dict[code]:
                for key in attribute:
                    _key = key
                    _temp_dict[_key] = attribute[_key]
            self.knowledge_dict[code] = _temp_dict


class MakeSocSkillsDict:

    def __init__(self):
        self.skills_dict = {}

    def read_skills(self, filename):
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            _attribute_list = []
            for row in csvreader:
                _dict = {}
                _list = []
                for value in row:
                    _list.append(value)
                soc_code = _list[0]
                attribute = _list[1]
                number = _list[2]
                _dict[attribute] = number
                _attribute_list.append(_dict)
                if len(_attribute_list) == 35:
                    self.skills_dict[soc_code] = _attribute_list
                    _attribute_list = []
        for code in self.skills_dict:
            _temp_dict = {}
            for attribute in self.skills_dict[code]:
                for key in attribute:
                    _key = key
                    _temp_dict[_key] = attribute[_key]
            self.skills_dict[code] = _temp_dict


class MakeSocAbilitiesDict:

    def __init__(self):
        self.abilities_dict = {}

    def read_abilities(self, filename):
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            _attribute_list = []
            for row in csvreader:
                _dict = {}
                _list = []
                for value in row:
                    _list.append(value)
                soc_code = _list[0]
                attribute = _list[1]
                number = _list[2]
                _dict[attribute] = number
                _attribute_list.append(_dict)
                if len(_attribute_list) == 52:
                    self.abilities_dict[soc_code] = _attribute_list
                    _attribute_list = []
        for code in self.abilities_dict:
            _temp_dict = {}
            for attribute in self.abilities_dict[code]:
                for key in attribute:
                    _key = key
                    _temp_dict[_key] = attribute[_key]
            self.abilities_dict[code] = _temp_dict


class MakeAverages:

    def __init__(self, mos_dict, knowledge_dict, skills_dict, abilities_dict):
        self.mos_dict = mos_dict
        self.knowledge_dict = knowledge_dict
        self.skills_dict = skills_dict
        self.abilities_dict = abilities_dict

    def make_knowledge_averages(self):
        knowledge_averages = {}
        knowledge_soc_with_values = {}
        for key1 in self.mos_dict:
            _soc_codes = self.mos_dict[key1]
            _soc_code_attributes = []
            for key2 in self.knowledge_dict:
                if key2 in _soc_codes:
                    _dict = {}
                    _dict[key2] = self.knowledge_dict[key2]
                    _soc_code_attributes.append(_dict)
            knowledge_soc_with_values[key1] = _soc_code_attributes
        for mos in knowledge_soc_with_values:
            attributes_list = []
            for code_dict in knowledge_soc_with_values[mos]:
                for code in code_dict:
                    attributes = code_dict[code]
                    attributes_list.append(attributes)
            key_list = set()
            for _dict2 in attributes_list:
                for attribute in _dict2:
                    key_list.add(attribute)
            _temp_dict = {}
            for key3 in key_list:
                avg = self.find_avg(attributes_list, key3)
                _temp_dict[key3] = avg
            knowledge_averages[mos] = _temp_dict
        knowledge_averages = dict([(k, v) for k, v in knowledge_averages.items() if len(v) > 0])
        return knowledge_averages

    def make_skill_averages(self):
        skill_averages = {}
        skill_soc_with_values = {}
        for key1 in self.mos_dict:
            _soc_codes = self.mos_dict[key1]
            _soc_code_attributes = []
            for key2 in self.skills_dict:
                if key2 in _soc_codes:
                    _dict = {}
                    _dict[key2] = self.skills_dict[key2]
                    _soc_code_attributes.append(_dict)
            skill_soc_with_values[key1] = _soc_code_attributes
        for mos in skill_soc_with_values:
            attributes_list = []
            for code_dict in skill_soc_with_values[mos]:
                for code in code_dict:
                    attributes = code_dict[code]
                    attributes_list.append(attributes)
            key_list = set()
            for _dict2 in attributes_list:
                for attribute in _dict2:
                    key_list.add(attribute)
            _temp_dict = {}
            for key3 in key_list:
                avg = self.find_avg(attributes_list, key3)
                _temp_dict[key3] = avg
            skill_averages[mos] = _temp_dict
        skill_averages = dict([(k, v) for k, v in skill_averages.items() if len(v) > 0])
        return skill_averages

    def make_ability_average(self):
        ability_averages = {}
        ability_soc_with_values = {}
        for key1 in self.mos_dict:
            _soc_codes = self.mos_dict[key1]
            _soc_code_attributes = []
            for key2 in self.abilities_dict:
                if key2 in _soc_codes:
                    _dict = {}
                    _dict[key2] = self.abilities_dict[key2]
                    _soc_code_attributes.append(_dict)
            ability_soc_with_values[key1] = _soc_code_attributes
        for mos in ability_soc_with_values:
            attributes_list = []
            for code_dict in ability_soc_with_values[mos]:
                for code in code_dict:
                    attributes = code_dict[code]
                    attributes_list.append(attributes)
            key_list = set()
            for _dict2 in attributes_list:
                for attribute in _dict2:
                    key_list.add(attribute)
            _temp_dict = {}
            for key3 in key_list:
                avg = self.find_avg(attributes_list, key3)
                _temp_dict[key3] = avg
            ability_averages[mos] = _temp_dict
        ability_averages = dict([(k, v) for k, v in ability_averages.items() if len(v) > 0])
        return ability_averages

    def find_avg(self, dict_list, key):
        total = 0

        for item in dict_list:
            total += float(item[key])

        return round(total / len(dict_list), 1)
