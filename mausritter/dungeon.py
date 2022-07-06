#dungeon.py
import utils
import chance_table_dungeon
import dice

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
        print("\tPuzzle Detail: " + chance_table_dungeon.puzzle_feature[dice.roll_1d6()-1])
    if room_type_str == "Lair":
        print("\tLair Detail: " + chance_table_dungeon.lair_feature[dice.roll_1d6()-1])

    print ("Creature Present: " + str(creature_present))
    print ("Treasure Present: " + str(treasure_present))
    if treasure_present:
        treasure_type = dice.roll_1d20() - 1
        treasure_type_str = chance_table_dungeon.treasure_type[treasure_type]
        print("\tTreasure Type: " + treasure_type_str)
        if treasure_type_str == "Magic Sword":
            print("\tMagic Sword Class: "+chance_table_dungeon.magic_sword_class[dice.roll_1d6()-1])
            print("\tMagic Sword Type: "+chance_table_dungeon.magic_sword_types[dice.roll_1d6()-1])
            magic_sword_cursed = chance_table_dungeon.magic_sword_cursed[dice.roll_1d6()-1]
            if magic_sword_cursed:
                print("\tMagic Sword Curse;Solution: "+chance_table_dungeon.cursed_sword_detail[dice.roll_1d6()-1])
    

def menu():
    exit = False;
    while exit != True:
        utils.print_header("Adventure-Site Menu")
        print("1 - Create New Room")
        print("0 - Main Menu")
        val = utils.get_input()
        if(val == 0):
            exit = True
        elif(val == 1):
            create_dungeon_room()
