import json
import re
import os
import sys
from model_attributes import weapon_attributes
# Add common libraries (one directory up)
current_dir = os.getcwd()
relative_path = '../'
absolute_path = os.path.abspath(os.path.join(current_dir, relative_path))
sys.path.append(absolute_path)
from common import dice

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
        
    def from_dict(self, data):
        #Populate data from data dictionary
        self.name = data['name'] 
        self.ap = data['ap']
        self.a = data['a']
        self.ranged = data['range']
        self.attributes = data['attributes'].copy()

    def roll_attacks(self, qual):
        hits = []
        for attack in range(self.a):
            roll = dice.roll_1d6()
            if roll >= qual:
                newHit = hit()
                hit.ap = self.ap
                hits.append(hit)
        return hits
