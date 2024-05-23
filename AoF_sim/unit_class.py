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

    def to_string(self):
        return (json.dumps(self.stats, indent=2))

    def gen_empty_stats(self):
        empty_stats = {}
        empty_stats['name'] = ''
        empty_stats['quality'] = 0
        empty_stats['defense'] = 0
        empty_stats['attacks'] = []
        empty_stats['models'] = 0
        empty_stats['impact'] = 0
        empty_stats['lance'] = False
        empty_stats['counter'] = False
        return empty_stats

    def charge(self, enemy_unit, fatigued=False, defender_fatigued=False):
        #TODO: Implement this as a single 'charge' simulation
        results = {}
        return results

    def shoot(self, enemy_unit):
        #TODO: Implement this as a single 'ranged attack' simulation
        results = {}
        return results
