#treasure.py
import dice
import treasure_tables

def print_treasure():
    text_array = roll_treasure()
    for line in text_array:
        print (line)

def check_magic_sword():
    magic_sword_cursed = treasure_tables.magic_sword_cursed[dice.roll_1d6()-1]
    if magic_sword_cursed:
        print("Oh no! The Sword is cursed!!")
        print("Curse; Solution: ["+treasure_tables.cursed_sword_detail[dice.roll_1d6()-1]+"]")
    else:
        print("Phew! no curse on this one")

def roll_treasure(treasure_type=100,tabs=0):
    text_array = []
    if treasure_type == 100:
        treasure_type = dice.roll_1d20() - 1
    indent=""
    for index in range(tabs):
        indent = indent+"\t"
    treasure_type_str = treasure_tables.treasure_type[treasure_type]
    text_array.append(indent+"Treasure Type: " + treasure_type_str)
    indent = indent+"\t"
    if treasure_type_str == "Magic Sword":
        text_array.append(indent+"Magic Sword Class: "+treasure_tables.magic_sword_class[dice.roll_1d6()-1])
        text_array.append(indent+"Magic Sword Type: "+treasure_tables.magic_sword_types[dice.roll_1d6()-1])
        text_array.append(indent+"HOPE IT'S NOT CURSED....")
    if treasure_type_str == "Random Spell":
        text_array.append(indent+"Spell Type: "+dice.roll_on_table(treasure_tables.spells))
    if treasure_type_str == "Trinket":
        treasure_str = dice.roll_on_table(treasure_tables.trinket)
        text_array.append(indent+"Trinket Detail: "+treasure_str)
        if "d6" in treasure_str.lower():
            text_array.append(indent+"d6 roll ["+str(dice.roll_1d6())+"]")
    if treasure_type_str == "Valuable Treasure":
        text_array.append(indent+"Valuable Treasure: "+treasure_tables.valuable[dice.roll_1d6()-1])
    if treasure_type_str == "Unusual Treasure":
        text_array.append(indent+"Unusual Treasure: "+treasure_tables.unusual[dice.roll_1d6()-1])
    if treasure_type_str == "Useful Treasure":
        treasure_str = dice.roll_on_table(treasure_tables.useful)
        text_array.append(indent+"Useful Treasure: "+treasure_str)
        if "d6" in treasure_str.lower():
            text_array.append(indent+"d6 roll ["+str(dice.roll_1d6())+"]")
    if treasure_type_str == "Large Treasure":
        text_array.append(indent+"Large Treasure: "+treasure_tables.large[dice.roll_1d6()-1])
    if treasure_type_str == "d6x100 pips":
        text_array.append(indent+"pips: " + str(dice.roll_1d6()*100))
    if treasure_type_str == "d6x50 pips":
        text_array.append(indent+"pips: " + str(dice.roll_1d6()*50))
    if treasure_type_str == "d6x10 pips":
        text_array.append(indent+"pips: " + str(dice.roll_1d6()*10))
    if treasure_type_str == "d6x5 pips":
        text_array.append(indent+"pips: " + str(dice.roll_1d6()*5))
    return text_array

def swchk(argv=[]):
    check_magic_sword()
    print()

def roltres(argv=[]):
    #roll_treasure()
    print_treasure()
    print()