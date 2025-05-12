import json

class report():
    def __init__(self):
        self.results = []
        self.average_damage = 0

    def add_result(self, result):
        self.results.append(result)
        totalDamage = 0
        for result in self.results:
            totalDamage += result.damage
        self.average_damage = totalDamage / len(self.results)
    
class result():
    def __init__(self):
        self.damage = 0