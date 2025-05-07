import json
import re
from model_class import model

class unit():
    def __init__(self):
        self.attributes = self.gen_empty_attributes()
        self.models = []
        self.name = ''
        self.quality = ''
        self.defense = ''

    def to_file(self, filename):
        #Outputs JSON string representing unit
        with open(filename, 'w') as fp:
            json.dump(self.to_dict(), fp, indent=2)

    def from_json(self, filename):
        # Load JSON
        temp_data = {}
        with open(filename) as json_file:
            temp_data = json.load(json_file)
        self.from_dict(temp_data)

    def from_unit_string_dict(self, unit_string_dict):
        #Takes raw input (parsed from army list pdf) and populates unit info
        if 'qua' not in unit_string_dict['string'].lower() or 'def' not in unit_string_dict['string'].lower():
            print('ERROR: Invalid Unit String')
            print(unit_string_dict)
            return
        self.name = unit_string_dict['name']
        #print(unit_string_dict)
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
        #Create models
        #Feed models the attribute/weapons string

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
        return data 

    def gen_empty_attributes(self):
        empty_data = {}
        return empty_data
