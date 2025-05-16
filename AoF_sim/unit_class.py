import json
import re
import os
import sys
from model_class import model
# Add common libraries (one directory up)
current_dir = os.getcwd()
relative_path = '../'
absolute_path = os.path.abspath(os.path.join(current_dir, relative_path))
sys.path.append(absolute_path)
from common import dice

class unit():
    def __init__(self):
        # Initializes empty object
        self.attributes = self.gen_empty_attributes()
        self.models = []
        self.name = ''
        self.quality = 0
        self.defense = 0

    def to_file(self, filename):
        #Outputs JSON file representing unit
        with open(filename, 'w') as fp:
            json.dump(self.to_dict(), fp, indent=2)

    def from_json(self, filename):
        # Loads all class data from JSON file
        temp_data = {}
        with open(filename) as json_file:
            temp_data = json.load(json_file)
        self.from_dict(temp_data)

    def from_unit_string_dict(self, unit_string_dict):
        #Takes raw input (DataDict parsed from army list pdf w/ pdf2dicts.py) and populates unit info
        if 'qua' not in unit_string_dict['string'].lower() or 'def' not in unit_string_dict['string'].lower():
            print('ERROR: Invalid Unit String')
            print(unit_string_dict)
            return
        self.name = unit_string_dict['name']
        #Get Qua/Def (format is Qua 1+  Def 2+; can split on + and pull numbers)
        qual_def_str = unit_string_dict['string'].split('+')
        self.quality = int(re.findall(r'\d+\.?\d*', qual_def_str[0])[0])
        self.defense = int(re.findall(r'\d+\.?\d*', qual_def_str[1])[0])
        #Remove Qual part of string
        index = unit_string_dict['string'].find('+')
        unitString = unit_string_dict['string'][index+1:]
        #Remove Def part of string
        index = unitString.find('+')
        unitString = unitString[index+1:]
        for modelIndex in range(unit_string_dict['models']):
            newModel = model(self.quality, self.defense)
            newModel.from_string(unitString)
            self.models.append(newModel)

    def to_dict(self):
        #Outputs Dictionary representing entire unit
        data = {}
        data['name'] = self.name
        data['quality'] = self.quality
        data['defense'] = self.defense
        data['attributes'] = self.attributes.copy()
        data['models'] = []
        for myModel in self.models:
            data['models'].append(myModel.to_dict())
        return data

    def from_dict(self, data):
        #Creates entire unit from data dictionary
        self.name = data['name']
        self.quality = data['quality']
        self.defense = data['defense']
        self.attributes = data['attributes'].copy()
        self.models = []
        for modelDict in data['models']:
            newModel = model(self.quality, self.defense)
            newModel.from_dict(modelDict)
            self.models.append(newModel)

    def gen_empty_attributes(self):
        #TODO any unit level attributes (not model level)
        empty_data = {}
        empty_data['regeneration']=False
        return empty_data

    def roll_attacks(self, ranged=False):
        hits = []
        for model in self.models:
            hits.extend(model.roll_attacks(ranged))
        return hits

    def roll_defense(self, hits, take_damage=False):
        damage = 0
        for hit in hits:
            roll = dice.roll_1d6()
            if roll == 6:
                continue
            if (roll-hit.ap) >= self.defense:
                continue
            if (self.attributes['regeneration'] and not hit.rending):
                roll_regen = dice.roll_1d6()
                if roll_regen >= 5:
                    continue
            damage += 1
        #TODO: Take Damage by killing off models
        return damage

