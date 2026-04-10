from pdf2dicts import convertPdf
import json
import csv

caleb_struct_default={
    'Faction':'Kriegsreich',
    'Unit':'',
    'Model Width':'1',
    'Model Length':'1',
    'Model Height':'2',
    'Model Qty':'',
    'Quality':'',
    'Defense':'',
    'Assigned Weapon':'',
    'Weapon qty per model':'1',
    'Cost':'',
    'Special Perks':'',
    ' ':'',
    '  ':'',
    'Weapon Name':'',
    'Weapon Type':'',
    'Weapon Perk':'',
    'Weapon Range':'',
    '   ':'',
    'Perk name':'',
    'Perk Description':'',
}

caleb_struct_empty={
    'Faction':'',
    'Unit':'',
    'Model Width':'',
    'Model Length':'',
    'Model Height':'',
    'Model Qty':'',
    'Quality':'',
    'Defense':'',
    'Assigned Weapon':'',
    'Weapon qty per model':'',
    'Cost':'',
    'Special Perks':'',
    ' ':'',
    '  ':'',
    'Weapon Name':'',
    'Weapon Type':'',
    'Weapon Perk':'',
    'Weapon Range':'',
    '   ':'',
    'Perk name':'',
    'Perk Description':'',
}

csvDictionary = {}
csvDictionaries = []
empire = convertPdf('ArmyBooks\Empire.pdf')
for unit in empire:
    #print(json.dumps(unit,indent=2))
    line_dict = caleb_struct_default.copy()
    line_dict['Unit'] = unit['Name']
    line_dict['Model Qty'] = unit['ModelCount']
    line_dict['Quality'] = 10-(2*(6-int(unit['Qual'])))
    line_dict['Defense'] = 10-(2*(6-int(unit['Def'])))
    line_dict['Assigned Weapon'] = ''
    for weapon in unit['Weapons']:
        line_dict['Assigned Weapon'] += weapon['Name'] + ';'
    line_dict['Assigned Weapon'] = line_dict['Assigned Weapon'].strip(';')
    line_dict['Special Perks'] = ''
    for perk in unit['Specs']:
        line_dict['Special Perks'] += perk + ';'
    line_dict['Special Perks'].strip(';')
    line_dict['Cost'] = unit['Cost']
    csvDictionaries.append(line_dict)
    #print(line_dict)
numberOfUnits = len(csvDictionaries)
unit_index = 0
unique_weapons = []
for unit in empire:
    for weapon in unit['Weapons']:
        if weapon['Name'] in unique_weapons:
            continue
        if unit_index < numberOfUnits:
            csvDictionaries[unit_index]['Weapon Name'] = weapon['Name']
            if 'range' in weapon.keys():
                csvDictionaries[unit_index]['Weapon Type'] = 'Ranged'
            else:
                csvDictionaries[unit_index]['Weapon Type'] = 'Melee'
            if 'AP' in weapon.keys():
                csvDictionaries[unit_index]['Weapon Perk'] = 'AP+('+str(weapon['AP'])+')'
            elif 'Specs' in weapon.keys() and weapon['Specs']:
                csvDictionaries[unit_index]['Weapon Perk'] = weapon['Specs'][0]
            unique_weapons.append(weapon['Name'])
            unit_index += 1
        else:
            newDict = caleb_struct_empty.copy()
            newDict['Weapon Name'] = weapon['Name']
            if 'range' in weapon.keys():
                newDict['Weapon Type'] = 'Ranged'
            else:
                newDict['Weapon Type'] = 'Melee'
            if 'AP' in weapon.keys():
                newDict['Weapon Perk'] = 'AP+('+str(weapon['AP'])+')'
            elif 'Specs' in weapon.keys() and weapon['Specs']:
                newDict['Weapon Perk'] = weapon['Specs'][0]
            csvDictionaries.append(newDict)
            unique_weapons.append(weapon['Name'])


with open('Empire.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=caleb_struct_empty.keys())
    dict_writer.writeheader()  # Writes the first row (column names)
    dict_writer.writerows(csvDictionaries) # Writes all dictionaries as rows