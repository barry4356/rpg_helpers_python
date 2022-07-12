#encounters.py
import dice
import utils
import additional_tables
import chance_table_encounter
import chance_table_dungeon
import random_adventure_table
import dungeon

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
    if "faerie" in creature_type.lower():
        print(indent+": Knows spell ["+dice.roll_on_table(chance_table_dungeon.spells)+"]")
    if "owl" in creature_type.lower():
        print(indent+": Knows spells ["+dice.roll_on_table(chance_table_dungeon.spells)+
            "] and ["+dice.roll_on_table(chance_table_dungeon.spells)+"]")


def adventure_generator():
    utils.print_header("Generated Adventure")
    creature_str = dice.roll_on_table(random_adventure_table.creature)
    problem_str = dice.roll_on_table(random_adventure_table.problem)
    complication_str = dice.roll_on_table(random_adventure_table.complication)
    print("The adventurers find a ["+creature_str+"] who ["+problem_str+"]. Unfortunately ["+complication_str+"].")
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