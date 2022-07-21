#encounters.py
import dice
import utils
import additional_tables
import chance_table_encounter
import chance_table_dungeon
import random_adventure_table
import dungeon
import treasure_tables
import treasure

def get_creature_detail(creature_name):
    for creature_shortname in chance_table_encounter.creatures:
        if creature_shortname in creature_name.lower():
            creature_name = creature_shortname
    return(chance_table_encounter.creature_details[creature_name.lower()])

def roll_encounter(tabs=0,is_dungeon_room=False):
    indent=""
    for index in range(tabs):
        indent = (indent+"\t")
    if(is_dungeon_room):
        indent = (indent+"Creature")
    else:
        indent = (indent+"Encounter")
    creature_roll = dice.roll_1d6()
    print(indent+" Roll: " + str(creature_roll))
    if creature_roll < 4:
        print(indent+": Common Encounter")
        creature_type_roll = dice.roll_1d10()-1
        creature_type = additional_tables.small[creature_type_roll]
        print(indent+" Selected (Experimental): "+creature_type)
    elif creature_roll < 6:
        print(indent+": Uncommon Encounter; Slightly Unusual")
        creature_type_roll = dice.roll_1d6()-1
        creature_type = ""
        if dice.coin_flip():
            creature_type = additional_tables.medium[creature_type_roll]
        else:
            creature_type = additional_tables.tiny[creature_type_roll]
        print(indent+" Selected (Experimental): "+creature_type)
    else:
        print(indent+": Strange or Dangerous Encounter")
        creature_type_roll = dice.roll_1d6()-1
        creature_type = additional_tables.large[creature_type_roll]
        print(indent+" Selected (Experimental): "+creature_type)
    reaction_roll = dice.roll_2d6()
    print(indent+": Reaction = "+chance_table_encounter.reactions[reaction_roll-2])
    detail_ary = get_creature_detail(creature_type)
    if "faerie" in creature_type.lower():
        print(indent+": Knows spell ["+dice.roll_on_table(treasure_tables.spells)+"]")
        detail_roll = dice.roll_1d6()
        print(indent+": Nefarious Plot: "+detail_ary[detail_roll-1][0]+", "+detail_ary[detail_roll-1][1])
    elif "owl" in creature_type.lower():
        print(indent+": Knows spells ["+dice.roll_on_table(treasure_tables.spells)+
            "] and ["+dice.roll_on_table(treasure_tables.spells)+"]")
        detail_roll = dice.roll_1d6()
        print(indent+": Optional NPC Roll: "+detail_ary[detail_roll-1][0]+", "+detail_ary[detail_roll-1][1])
    elif "crow" in creature_type.lower():
        song_roll1 = dice.roll_1d6()
        song_roll2 = dice.roll_1d6()
        while song_roll1 == song_roll2:
            song_roll2 = dice.roll_1d6()
        print(indent+": Knows songs ["+str(detail_ary[song_roll1-1][0])+
            "] and ["+str(detail_ary[song_roll2-1][0])+"]")
        print(indent+":\t"+detail_ary[song_roll1-1][0]+": "+detail_ary[song_roll1-1][1])
        print(indent+":\t"+detail_ary[song_roll2-1][0]+": "+detail_ary[song_roll2-1][1])
    elif "cat" in creature_type.lower() or "frog" in creature_type.lower() or "mouse" in creature_type.lower():
        detail_roll = dice.roll_1d6()
        print(indent+": Optional NPC Roll: "+detail_ary[detail_roll-1][0]+", "+detail_ary[detail_roll-1][1])
    else:
        print(detail_ary)
        detail_roll = dice.roll_1d6()
        print(indent+": Optional Creature Sub-Type Roll: "+detail_ary[detail_roll-1][0]+", "+detail_ary[detail_roll-1][1])


def adventure_generator():
    utils.print_header("Generated Adventure")
    creature_str = dice.roll_on_table(random_adventure_table.creature)
    problem_str = dice.roll_on_table(random_adventure_table.problem)
    complication_str = dice.roll_on_table(random_adventure_table.complication)
    print("The adventurers find a ["+creature_str+"] who ["+problem_str+"]. Unfortunately ["+complication_str+"].")
    print("The ["+creature_str+"] Offers a reward of:")
    treasure.roll_treasure(treasure_type=10,tabs=1)
    print("Can our brave mice sally forth to solve this dilema?")

def check_encounter():
    print("Rolling Encounter Check (Encounter, Omen, None)...")
    encounter_roll = dice.roll_1d6()
    print("Encounter Roll: ["+str(encounter_roll)+"]")
    if encounter_roll == 1:
        print("Random Encounter!")
        dungeon.print_encounter()
    elif encounter_roll == 2:
        print("Rolled Omen")
    else:
        print("No Encounter")