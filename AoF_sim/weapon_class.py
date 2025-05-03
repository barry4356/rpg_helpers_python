import json


class weapon():
    def __init__(self):
        self.data = self.gen_empty_data()

    def gen_empty_data(self):
        data = {
        'ap': 0,
        'a': 0,
        'poison': False,
        'range': 0,
        }
        return data
        
    def from_string(self, weapon_string):
        #Break out the weapons
        print(weapon_string)
