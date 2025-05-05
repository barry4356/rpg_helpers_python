import json
import re

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
        attackStrPattern = re.escape('A') + r"(\d+)"
        match = re.search(attackStrPattern, weapon_string)
        if match:
            self.data['a'] = int(match.group(1))
        apStrPattern = re.escape('AP(') + r"(\d+)"
        match = re.search(apStrPattern, weapon_string)
        if match:
            self.data['ap'] = int(match.group(1))

    def to_string(self):
        return json.dumps(self.data, indent=2)