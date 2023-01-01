from collections import Counter

class calculateDifferences:

    def __init__(self, knowledge_averages, ideal_knowledge,
                 skill_averages, ideal_skills,
                 ability_averages, ideal_abilities):
        self.knowledge = self.calculate(knowledge_averages, ideal_knowledge)
        self.skill = self.calculate(skill_averages, ideal_skills)
        self.ability = self.calculate(ability_averages, ideal_abilities)

    def calculate(self, average_dict, ideal_dict):
        difference = {}
        for mos in average_dict:
            d1 = average_dict[mos]
            d2 = ideal_dict
            d3 = {}

            for k, v in d1.items():
                d3[k] = v - d2.get(k, 0)
            d4 = {}
            for key in d3:
                d4[key] = round(d3[key], 1)
            difference[mos] = d4
        return difference

class addUpDifferences:

    def __init__(self, total_knowledge, total_skill, total_ability):
        self.total_for_all_mos = {}
        total_knowledge_per_mos = self.total_per(total_knowledge)
        total_skill_per_mos = self.total_per(total_skill)
        total_ability_per_mos = self.total_per(total_ability)

        for key in total_knowledge_per_mos:
             self.total_for_all_mos[key] = round(total_knowledge_per_mos[key] + total_skill_per_mos[key] + total_ability_per_mos[key], 1)

    def total_per(self, _dict):
        for mos in _dict:
            values = list(_dict[mos].values())
            total = sum(values)
            _dict[mos] = total
        return _dict

