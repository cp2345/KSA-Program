from src import MakeDict

mos = MakeDict.MosDict()
knowledge = MakeDict.MakeSocKnowledgeDict()
skills = MakeDict.MakeSocSkillsDict()
abilities = MakeDict.MakeSocAbilitiesDict()

mos.read_mos('resources/MOS_to_SOC.csv')
knowledge.read_knowledge('resources/Knowledge.csv')
skills.read_skills('resources/Skills.csv')
abilities.read_abilities('resources/Abilities.csv')

average = MakeDict.MakeAverages(mos.mos_dict, knowledge.knowledge_dict, skills.skills_dict, abilities. abilities_dict)
knowledge_averages = average.make_knowledge_averages()
skill_averages = average.make_skill_averages()
ability_averages = average.make_ability_average()



