import json


class unit():
    def __init__(self):
        self.stats = self.gen_empty_stats()

    def to_file(self, filename):
        with open(filename, 'w') as fp:
            json.dump(self.stats, fp, indent=2)

    def from_file(self, filename):
        empty_stats = self.gen_empty_stats()
        temp_stats = {}
        with open(filename) as json_file:
            temp_stats = json.load(json_file)
        self.stats = empty_stats
        for mykey in self.stats:
            if mykey in temp_stats.keys():
                self.stats[mykey] = temp_stats[mykey]
            elif mykey in empty_stats.keys():
                self.stats[mykey] = empty_stats[mykey]
        if 'units' not in temp_stats.keys():
            return
        new_units = []
        empty_unit = self.gen_empty_unit()
        for temp_unit in temp_stats['units']:
            new_unit = {}
            for mykey in empty_unit:
                if mykey in temp_unit.keys():
                    new_unit[mykey] = temp_unit[mykey]
                else:
                    new_unit[mykey] = empty_unit[mykey]
            new_units.append(new_unit)
        self.stats['units'] = new_units
            

    def to_string(self):
        return (json.dumps(self.stats, indent=2))

    def gen_empty_unit(self):
        empty_unit = {}
        empty_unit['name'] = ''
        empty_unit['quality'] = 0
        empty_unit['defense'] = 0
        empty_unit['attacks'] = []
        empty_unit['models'] = 0
        empty_unit['impact'] = 0
        empty_unit['lance'] = False
        empty_unit['counter'] = False
        return empty_unit

    def gen_empty_stats(self):
        empty_stats = {}
        empty_stats['name'] = ''
        empty_stats['units'] = []
        return empty_stats

    def charge(self, enemy_unit, fatigued=False, defender_fatigued=False):
        #TODO: Implement this as a single 'charge' simulation
        results = {}
        return results

    def shoot(self, enemy_unit):
        #TODO: Implement this as a single 'ranged attack' simulation
        results = {}
        return results
