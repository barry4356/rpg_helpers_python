#encounters.py
import dice
import additional_tables
import chance_table_encounter

def roll_encounter(tabs=0):
    indent=""
    for index in range(tabs):
        indent = (indent+"\t")
    creature_roll = dice.roll_1d6()
    print(indent+"Creature Roll: " + str(creature_roll))
    if creature_roll < 4:
        print(indent+"Creature: Common Encounter")
        creature_type_roll = dice.roll_1d10()-1
        print(indent+"Creature Selected (Experimental): "+additional_tables.small[creature_type_roll])
    elif creature_roll < 6:
        print(indent+"Creature: Uncommon Encounter; Slightly Unusual")
        creature_type_roll = dice.roll_1d6()-1
        creature_type = ""
        if dice.coin_flip():
            creature_type = additional_tables.medium[creature_type_roll]
        else:
            creature_type = additional_tables.tiny[creature_type_roll]
        print(indent+"Creature Selected (Experimental): "+creature_type)

    else:
        print(indent+"Creature: Strange or Dangerous Encounter")
        creature_type_roll = dice.roll_1d6()-1
        print(indent+"Creature Selected (Experimental): "+additional_tables.large[creature_type_roll])

    reaction_roll = dice.roll_2d6()
    print(indent+"Creature: Reaction = "+chance_table_encounter.reactions[reaction_roll-2])