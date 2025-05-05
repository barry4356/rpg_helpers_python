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
        'name': '',
        }
        return data
        
    def from_string(self, weapon_string):
        #Break out the weapons
        weaponStrAry = weapon_string.split('(')
        self.data['name'] = weaponStrAry[0].replace(' ','')
        weaponStrAry = weapon_string.split('(A')
        self.data['a'] = weaponStrAry[1][0]
        weaponStrAry = weapon_string.split('AP(')
        self.data['ap'] = weaponStrAry[1][0]

    def to_string(self):
        return json.dumps(self.data, indent=2)