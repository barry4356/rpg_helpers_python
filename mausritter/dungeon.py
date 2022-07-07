#dungeon.py
import utils
import chance_table_dungeon
import dice
import additional_tables

def roll_encounter():
    utils.print_header("Encounter")
    creature_roll = dice.roll_1d6()
    print("Creature Roll: " + str(creature_roll))
    if creature_roll < 4:
        print("Creature: Common Encounter")
        creature_type_roll = dice.roll_1d10()-1
        print("Creature Selected (Experimental): "+additional_tables.small[creature_type_roll])
    elif creature_roll < 6:
        print("Creature: Uncommon Encounter; Slightly Unusual")
        creature_type_roll = dice.roll_1d6()-1
        creature_type = ""
        if dice.coin_flip():
            creature_type = additional_tables.medium[creature_type_roll]
        else:
            creature_type = additional_tables.tiny[creature_type_roll]
        print("Creature Selected (Experimental): "+creature_type)

    else:
        print("Creature: Strange or Dangerous Encounter")
        creature_type_roll = dice.roll_1d6()-1
        print("Creature Selected (Experimental): "+additional_tables.large[creature_type_roll])

    reaction_roll = dice.roll_2d6()
    print("Creature: Reaction = "+chance_table_dungeon.reactions[reaction_roll-2])

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
        print("\tPuzzle Detail: " + chance_table_dungeon.puzzle_feature[puzzle_feature_number])
        if puzzle_feature_number == 0 or puzzle_feature_number == 2 or puzzle_feature_number == 3 or puzzle_feature_number == 4:
            print("\tPUZZLE HAS TREASURE!!")
            treasure_type = dice.roll_1d20() - 1
            if puzzle_feature_number == 2:
                treasure_type = 0
            treasure_type_str = chance_table_dungeon.treasure_type[treasure_type]
            print("\t\tPuzzle Treasure Type: " + treasure_type_str)
            if treasure_type_str == "Magic Sword":
                print("\t\tMagic Sword Class: "+chance_table_dungeon.magic_sword_class[dice.roll_1d6()-1])
                print("\t\tMagic Sword Type: "+chance_table_dungeon.magic_sword_types[dice.roll_1d6()-1])
                magic_sword_cursed = chance_table_dungeon.magic_sword_cursed[dice.roll_1d6()-1]
                if magic_sword_cursed:
                    print("\t\tMagic Sword Curse;Solution: "+chance_table_dungeon.cursed_sword_detail[dice.roll_1d6()-1])
            if treasure_type_str == "Random Spell":
                print("\t\tSpell Type: "+chance_table_dungeon.spells[dice.roll_1d15()-1])
            if treasure_type_str == "Trinket":
                print("\t\tTrinket Detail: "+chance_table_dungeon.trinket[dice.roll_1d6()-1])
            if treasure_type_str == "Valuable Treasure":
                print("\t\tValuable Treasure: "+chance_table_dungeon.valuable[dice.roll_1d6()-1])
            if treasure_type_str == "Unusual Treasure":
                print("\t\tUnusual Treasure: "+chance_table_dungeon.unusual[dice.roll_1d6()-1])
            if treasure_type_str == "Useful Treasure":
                print("\t\tUseful Treasure: "+chance_table_dungeon.useful[dice.roll_1d6()-1])
            if treasure_type_str == "Large Treasure":
                print("\t\tLarge Treasure: "+chance_table_dungeon.large[dice.roll_1d6()-1])
            if treasure_type_str == "d6x100 pips":
                print("\t\tpips: " + str(dice.roll_1d6()*100))
            if treasure_type_str == "d6x50 pips":
                print("\t\tpips: " + str(dice.roll_1d6()*50))
            if treasure_type_str == "d6x10 pips":
                print("\t\tpips: " + str(dice.roll_1d6()*10))
            if treasure_type_str == "d6x5 pips":
                print("\t\tpips: " + str(dice.roll_1d6()*5))   


    if room_type_str == "Lair":
        print("\tLair Detail: " + chance_table_dungeon.lair_feature[dice.roll_1d6()-1])

    print ("-\nCreature Present: " + str(creature_present))
    if creature_present:
        creature_roll = dice.roll_1d6()
        print("\tCreature Roll: " + str(creature_roll))
        if creature_roll < 4:
            print("\tCreature: Common Encounter")
            creature_type_roll = dice.roll_1d10()-1
            print("\tCreature Selected (Experimental): "+additional_tables.small[creature_type_roll])
        elif creature_roll < 6:
            print("\tCreature: Uncommon Encounter; Slightly Unusual")
            creature_type_roll = dice.roll_1d6()-1
            creature_type = ""
            if dice.coin_flip():
                creature_type = additional_tables.medium[creature_type_roll]
            else:
                creature_type = additional_tables.tiny[creature_type_roll]
            print("\tCreature Selected (Experimental): "+creature_type)
        else:
            print("\tCreature: Strange or Dangerous Encounter")
            creature_type_roll = dice.roll_1d6()-1
            print("\tCreature Selected (Experimental): "+additional_tables.large[creature_type_roll])

        reaction_roll = dice.roll_2d6()
        print("\tCreature: Reaction = "+chance_table_dungeon.reactions[reaction_roll-2])


    print ("-\nTreasure Present: " + str(treasure_present))
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
        if treasure_type_str == "Random Spell":
            print("\tSpell Type: "+chance_table_dungeon.spells[dice.roll_1d15()-1])
        if treasure_type_str == "Trinket":
             print("\tTrinket Detail: "+chance_table_dungeon.trinket[dice.roll_1d6()-1])
        if treasure_type_str == "Valuable Treasure":
             print("\tValuable Treasure: "+chance_table_dungeon.valuable[dice.roll_1d6()-1])
        if treasure_type_str == "Unusual Treasure":
             print("\tUnusual Treasure: "+chance_table_dungeon.unusual[dice.roll_1d6()-1])
        if treasure_type_str == "Useful Treasure":
             print("\tUseful Treasure: "+chance_table_dungeon.useful[dice.roll_1d6()-1])
        if treasure_type_str == "Large Treasure":
             print("\tLarge Treasure: "+chance_table_dungeon.large[dice.roll_1d6()-1])
        if treasure_type_str == "d6x100 pips":
            print("\tpips: " + str(dice.roll_1d6()*100))
        if treasure_type_str == "d6x50 pips":
            print("\tpips: " + str(dice.roll_1d6()*50))
        if treasure_type_str == "d6x10 pips":
            print("\tpips: " + str(dice.roll_1d6()*10))
        if treasure_type_str == "d6x5 pips":
            print("\tpips: " + str(dice.roll_1d6()*5))    

def menu():
    func_list = [create_dungeon_room, roll_encounter]
    desc_list = ["Create New Room", "Roll Encounter"]
    utils.menu(func_list,desc_list,"Adventure-Site Menu",False)
