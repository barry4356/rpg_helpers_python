import json

class unit():
    def __init__(self):
        self.data = self.gen_empty_data()

    def to_file(self, filename):
        with open(filename, 'w') as fp:
            json.dump(self.data, fp, indent=2)

    def from_file(self, filename):
        # Load JSON
        empty_data = self.gen_empty_data()
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
        self.data['models'] = new_models

    def from_raw(self, unit_string):
        #Takes raw input (parsed from army list pdf) and populates unit info
        if 'qua' not in unit_string.lower() or 'def' not in unit_string.lower():
            print('ERROR: Invalid Unit String')
            print(unit_string)
            return

    def to_string(self):
        #Outputs JSON string representing unit
        return (json.dumps(self.data, indent=2))

    def gen_empty_weapon(self):
        empty_weapon = {}
        empty_weapon['name'] = ''
        empty_weapon['hits'] = 0
        empty_weapon['ranged'] = False
        empty_weapon['melee'] = False
        empty_weapon['ap'] = 0
        empty_weapon['range'] = 0
        return empty_weapon

    def gen_empty_model(self):
        empty_model = {}
        empty_model['name'] = ''
        empty_model['quality'] = 0
        empty_model['defense'] = 0
        empty_model['weapons'] = []
        empty_model['impact'] = 0
        empty_model['lance'] = False
        empty_model['counter'] = False
        empty_model['furious'] = False
        empty_model['furiouser'] = False
        return empty_model

    def gen_empty_data(self):
        empty_data = {}
        empty_data['name'] = ''
        empty_data['models'] = []
        empty_data['quality'] = 0
        empty_data['defense'] = 0
        empty_data['stats'] = {}
        return empty_data
