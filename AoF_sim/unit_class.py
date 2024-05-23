import json


class unit():
    def __init__(self):
        self.stats = self.gen_empty_stats()

    def to_file(self, filename):
        with open(filename, 'w') as fp:
            json.dump(self.stats, fp, indent=2)

    def from_file(self, filename):
        # Load JSON
        empty_stats = self.gen_empty_stats()
        temp_stats = {}
        with open(filename) as json_file:
            temp_stats = json.load(json_file)
        self.stats = empty_stats
        # Load Top Level Stats
        for mykey in self.stats:
            if mykey in temp_stats.keys():
                self.stats[mykey] = temp_stats[mykey]
            elif mykey in empty_stats.keys():
                self.stats[mykey] = empty_stats[mykey]
        # Check for models
        if 'models' not in temp_stats.keys():
            return
        new_models = []
        empty_model = self.gen_empty_model()
        # Load each model
        for temp_model in temp_stats['models']:
            new_model = {}
            for mykey in empty_model:
                if mykey in temp_model.keys():
                    new_model[mykey] = temp_model[mykey]
                else:
                    new_model[mykey] = empty_model[mykey]
            #TODO Handle each weapon
            new_models.append(new_model)
        self.stats['models'] = new_models
            
    def to_string(self):
        return (json.dumps(self.stats, indent=2))

    def gen_empty_weapon(self):
        empty_weapon = {}
        empty_weapon['name'] = ''
        empty_weapon['hits'] = 0
        empty_weapon['ranged'] = False
        empty_weapon['melee'] = False
        empty_weapon['ap'] = 0
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

    def gen_empty_stats(self):
        empty_stats = {}
        empty_stats['name'] = ''
        empty_stats['models'] = []
        return empty_stats
