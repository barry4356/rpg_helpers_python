#dungeon.py
import utils
import chance_table_dungeon
import dice
import additional_tables
import encounters
import contracts

def print_encounter():
    utils.print_header("Encounter")
    encounters.roll_encounter()

def check_magic_sword():
    magic_sword_cursed = chance_table_dungeon.magic_sword_cursed[dice.roll_1d6()-1]
    if magic_sword_cursed:
        print("Oh no! The Sword is cursed!!")
        print("Curse; Solution: ["+chance_table_dungeon.cursed_sword_detail[dice.roll_1d6()-1]+"]")
    else:
        print("Phew! no curse on this one")

def roll_treasure(treasure_type=100,tabs=0):
    if treasure_type == 100:
        treasure_type = dice.roll_1d20() - 1
    indent=""
    for index in range(tabs):
        indent = indent+"\t"
    treasure_type_str = chance_table_dungeon.treasure_type[treasure_type]
    print(indent+"Treasure Type: " + treasure_type_str)
    if treasure_type_str == "Magic Sword":
        print(indent+"Magic Sword Class: "+chance_table_dungeon.magic_sword_class[dice.roll_1d6()-1])
        print(indent+"Magic Sword Type: "+chance_table_dungeon.magic_sword_types[dice.roll_1d6()-1])
        print(indent+"HOPE IT'S NOT CURSED....")
    if treasure_type_str == "Random Spell":
        print(indent+"Spell Type: "+dice.roll_on_table(chance_table_dungeon.spells))
    if treasure_type_str == "Trinket":
        treasure_str = dice.roll_on_table(chance_table_dungeon.trinket)
        print(indent+"Trinket Detail: "+treasure_str)
        if "d6" in treasure_str.lower():
            print (indent+"d6 roll ["+str(dice.roll_1d6())+"]")
    if treasure_type_str == "Valuable Treasure":
        print(indent+"Valuable Treasure: "+chance_table_dungeon.valuable[dice.roll_1d6()-1])
    if treasure_type_str == "Unusual Treasure":
        print(indent+"Unusual Treasure: "+chance_table_dungeon.unusual[dice.roll_1d6()-1])
    if treasure_type_str == "Useful Treasure":
        treasure_str = dice.roll_on_table(chance_table_dungeon.useful)
        print(indent+"Useful Treasure: "+treasure_str)
        if "d6" in treasure_str.lower():
            print (indent+"d6 roll ["+str(dice.roll_1d6())+"]")
    if treasure_type_str == "Large Treasure":
        print(indent+"Large Treasure: "+chance_table_dungeon.large[dice.roll_1d6()-1])
    if treasure_type_str == "d6x100 pips":
        print(indent+"pips: " + str(dice.roll_1d6()*100))
    if treasure_type_str == "d6x50 pips":
        print(indent+"pips: " + str(dice.roll_1d6()*50))
    if treasure_type_str == "d6x10 pips":
        print(indent+"pips: " + str(dice.roll_1d6()*10))
    if treasure_type_str == "d6x5 pips":
        print(indent+"pips: " + str(dice.roll_1d6()*5))   

def create_dungeon_room():
    utils.print_header("Room")
    room_type = dice.roll_1d6() - 1
    room_type_str = chance_table_dungeon.room_type[room_type]
    creature_present = chance_table_dungeon.creature_present[room_type][dice.roll_1d6()-1]
    treasure_present = chance_table_dungeon.treasure_present[room_type][dice.roll_1d6()-1]
    print ("Room Type: " + room_type_str)
    if room_type_str == "Empty":
        print("\tEmpty Detail: " + chance_table_dungeon.empty_feature[dice.roll_1d20()-1])
    if room_type_str == "Obstacle":
        print("\tObstacle Detail: " + chance_table_dungeon.obstacle_feature[dice.roll_1d8()-1])
    if room_type_str == "Trap":
        print("\tTrap Detail: " + chance_table_dungeon.trap_feature[dice.roll_1d8()-1])
    if room_type_str == "Puzzle":
        puzzle_feature_number = dice.roll_1d6()-1
        puzzle_detail = chance_table_dungeon.puzzle_feature[puzzle_feature_number]
        print("\tPuzzle Detail: " + puzzle_detail)
        if "treasure" in puzzle_detail.lower() or "sword" in puzzle_detail.lower() :
            print("\tPUZZLE HAS TREASURE!!")
            if "sword" in puzzle_detail.lower():
                treasure_type_index = 0
            else:
                treasure_type_index = dice.roll_1d20() - 1
            roll_treasure(treasure_type=treasure_type_index,tabs=2)
    if room_type_str == "Lair":
        print("\tLair Detail: " + chance_table_dungeon.lair_feature[dice.roll_1d6()-1])
    print ("-\nCreature Present: " + str(creature_present))
    if creature_present:
        encounters.roll_encounter(tabs=1,is_dungeon_room=True)
    print ("-\nTreasure Present: " + str(treasure_present))
    if treasure_present:
        roll_treasure(tabs=1)

def menu():
    func_list = [create_dungeon_room, encounters.check_encounter, encounters.adventure_generator,roll_treasure,check_magic_sword,contracts.print_contract]
    desc_list = ["Create New Room","Roll for Encounter", "Random Adventure","Roll Random Treasure","Check sword for curse","Check Wanted Poster"]
    utils.menu(func_list,desc_list,"Adventure Menu",False)
