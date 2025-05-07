import json
from weapon_class import weapon
from model_attributes import base_attributes
import re
import sys

class model():
    def __init__(self, qual, defense):
        self.attributes = self.gen_empty_attributes()
        self.quality = qual
        self.defense = defense
        self.weapons = []

    def gen_empty_attributes(self):
        attributes = base_attributes.copy()
        return attributes
        
    def from_string(self, model_string):
        #Break out the weapons by finding the first attribute keyword in the string
        model_string = model_string.replace(')', ') ').replace('  ',' ')
        words = model_string.split(' ')
        firstAttribute = None
        for attribute in base_attributes.keys():
            for word in words:
                if attribute.lower() in word.lower():
                    firstAttribute = attribute
                    break
            if firstAttribute:
                break
        weaponString = model_string
        attributeString = None
        if firstAttribute:
            weaponString = re.split(firstAttribute, model_string, flags=re.IGNORECASE)[0]
            attributeString = firstAttribute + re.split(firstAttribute, model_string, flags=re.IGNORECASE)[1]
        
        weaponsParsed = False
        weaponStringRemaining = weaponString
        weaponArry = []
        while not weaponsParsed:
            opened = 0
            closed = 0
            splitPoint = 0
            for index, letter in enumerate(weaponStringRemaining):
                if letter == '(':
                    opened += 1
                if letter == ')':
                    closed += 1
                if opened > 0 and closed > 0 and opened == closed:
                    splitPoint = index
                    break
            weaponArry.append(weaponStringRemaining[:index+1])
            weaponStringRemaining = weaponStringRemaining[index+1:]
            if '(' not in weaponStringRemaining:
                if len(weaponStringRemaining) > 1:
                    weaponArry.append(weaponStringRemaining)
                weaponsParsed = True

        if attributeString:
            attributeString = attributeString.replace(',',' ').replace('  ',' ').lower()
            for attributeStr in attributeString.split(' '):
                for attributeKey in self.attributes.keys():
                    if attributeKey in attributeStr:
                        if type(self.attributes[attributeKey]) is bool:
                            self.attributes[attributeKey] = True
                        elif type(self.attributes[attributeKey]) is int:
                            if '(' in attributeStr and ')' in attributeStr:
                                self.attributes[attributeKey] += int(attributeStr.split(')')[0].split('(')[-1])
                            
        for weaponStr in weaponArry:
            newWeapon = weapon()
            newWeapon.from_string(weaponStr)
            self.weapons.append(newWeapon)

    def to_dict(self):
        data = {}
        data['quality'] = self.quality
        data['defense'] = self.defense
        data['attributes'] = self.attributes.copy()
        data['weapons'] = []
        for weapon in self.weapons:
            data['weapons'].append(weapon.to_dict())
        return data