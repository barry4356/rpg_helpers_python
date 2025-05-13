import json
import re
import os
import sys
from model_attributes import weapon_attributes
from hit_class import hit
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
        for weapon_attribute in self.attributes.keys():
            if weapon_attribute.lower() in weapon_string.lower():
                if type(self.attributes[weapon_attribute]) is bool:
                    self.attributes[weapon_attribute] = True
                elif type(self.attributes[weapon_attribute]) is int:
                    pass
                    #TODO: Model this... look how model_class handles AP

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

    def roll_attacks(self, wielder):
        hits = []
        # Reliable weapons count as Quality 2+
        if self.attributes['reliable']:
            qual = 2
        # Roll each attack
        for attack in range(self.a):
            roll = dice.roll_1d6()
            if roll >= wielder.quality or roll >= 6:
                newHit = hit()
                newHit.ap = self.ap
                # Rending creates AP(4) on nat 6
                if self.attributes['rending']:
                    newHit.rending = True
                    if roll >= 6:
                        newHit.ap = 4
                hits.append(newHit)
                if roll >= 6 and wielder.attributes['furious']:
                    furiousHit = hit()
                    furiousHit.ap = self.ap
                    furiousHit.rending = self.attributes['rending']
                    hits.append(furiousHit)
        return hits
