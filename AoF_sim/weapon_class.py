import json
import re
from model_attributes import weapon_attributes

class weapon():
    def __init__(self):
        self.attributes = self.gen_empty_attributes()
        self.ap = 0
        self.a = 0
        self.ranged = 0
        self.name = ''

    def gen_empty_attributes(self):
        attributes = weapon_attributes.copy()
        return attributes
        
    def from_string(self, weapon_string):
        #Break out the weapons
        weaponStrAry = weapon_string.split('(')
        self.name = weaponStrAry[0].replace(' ','')
        attackStrPattern = re.escape('A') + r"(\d+)"
        match = re.search(attackStrPattern, weapon_string)
        if match:
            self.a = int(match.group(1))
        apStrPattern = re.escape('AP(') + r"(\d+)"
        match = re.search(apStrPattern, weapon_string)
        if match:
            self.ap = int(match.group(1))

    def to_dict(self):
        data = {}
        data['name'] = self.name
        data['ap'] = self.ap
        data['a'] = self.a
        data['range'] = self.ranged
        data['attributes']  = self.attributes.copy()
        return data