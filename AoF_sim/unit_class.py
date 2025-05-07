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
        empty_data = self.gen_empty_attributes()
        temp_data = {}
        with open(filename) as json_file:
            temp_data = json.load(json_file)
        self.data = empty_data
        # Load Top Level Data
        for mykey in self.data:
            if mykey in temp_data.keys():
                self.data[mykey] = temp_data[mykey]
            elif mykey in empty_data.keys():
                self.data[mykey] = empty_data[mykey]
        # Check for models
        if 'models' not in temp_data.keys():
            return
        new_models = []
        empty_model = self.gen_empty_model()
        # Load each model
        for temp_model in temp_data['models']:
            new_model = {}
            for mykey in empty_model:
                # Populate model from file; use empty instance for missing keys
                if mykey in temp_model.keys():
                    new_model[mykey] = temp_model[mykey]
                else:
                    new_model[mykey] = empty_model[mykey]
            # Populate weapons from file; use empty instance for missing keys
            empty_weapon = self.gen_empty_weapon()
            if 'weapons' in temp_model.keys():
                for temp_weapon in temp_model['weapons']:
                    for weapkey in empty_weapon:
                        if weapkey not in temp_weapon.keys():
                            temp_weapon[weapkey] = empty_weapon[weapkey]
            new_models.append(new_model)
        self.models = new_models
        #TODO Re-evaluate this function after a JSON is created from the PDF List

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
        #Outputs JSON string representing unit
        data = {}
        data['name'] = self.name
        data['quality'] = self.quality
        data['defense'] = self.defense
        data['attributes'] = self.attributes.copy()
        data['models'] = []
        for myModel in self.models:
            data['models'].append(myModel.to_dict())
        return data

    def gen_empty_attributes(self):
        empty_data = {}
        return empty_data
