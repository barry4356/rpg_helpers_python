#dungeon.py
import utils
import chance_table_dungeon
import creature_tables
import dice
import additional_tables
import encounters
import contracts
import treasure
import treasure_tables

def print_encounter():
    utils.print_header("Encounter")
    encounters.roll_encounter()

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
            treasure.roll_treasure(treasure_type=treasure_type_index,tabs=2)
    if room_type_str == "Lair":
        print("\tLair Detail: " + chance_table_dungeon.lair_feature[dice.roll_1d6()-1])
    print ("-\nCreature Present: " + str(creature_present))
    if creature_present:
        encounters.roll_encounter(tabs=1,is_dungeon_room=True)
    print ("-\nTreasure Present: " + str(treasure_present))
    if treasure_present:
        treasure.roll_treasure(tabs=1)

def print_stats(stats):
    hp = stats[0]
    strength = stats[1]
    dex = stats[2]
    wil = stats[3]
    arm = stats[4]
    atk_str = stats[5]
    wants_str = stats[6]
    print("HP: "+str(hp)+" STR: "+str(strength)+" DEX: "+str(dex)
            +" WIL: "+str(wil)+" Armor: "+str(arm))
    print("Attack: "+atk_str)

def print_creature_detail(creature):
    detail_ary = encounters.get_creature_detail(creature)
    if "faerie" in creature.lower():
        print("Knows spell ["+dice.roll_on_table(treasure_tables.spells)+"]")
    if "owl" in creature.lower():
        print("Knows spells ["+dice.roll_on_table(treasure_tables.spells)+
            "] and ["+dice.roll_on_table(treasure_tables.spells)+"]")
    if "crow" in creature.lower():
        song_roll1 = dice.roll_1d6()
        song_roll2 = dice.roll_1d6()
        while song_roll1 == song_roll2:
            song_roll2 = dice.roll_1d6()
        print("Knows songs ["+str(detail_ary[song_roll1-1][0])+
            "] and ["+str(detail_ary[song_roll2-1][0])+"]")
        print("\t"+detail_ary[song_roll1-1][0]+": "+detail_ary[song_roll1-1][1])
        print("\t"+detail_ary[song_roll2-1][0]+": "+detail_ary[song_roll2-1][1])
    detail_roll = dice.roll_1d6()
    print("Detail:\n"+detail_ary[detail_roll-1][0]+":\t"+detail_ary[detail_roll-1][1])
    print ("")

def roll_creature_menu():
    header = "Roll a Creature"
    creature = utils.array_select_menu(array=creature_tables.creatures,header=header)
    if not creature:
        return
    print(creature+" Stats")
    print_stats(creature_tables.enemy_stats[creature])
    print_creature_detail(creature)
    roll_creature_menu()


def menu():
    func_list = [create_dungeon_room, encounters.check_encounter, encounters.adventure_generator,
        treasure.roll_treasure,treasure.check_magic_sword,contracts.print_contract]
    desc_list = ["Create New Room","Roll for Encounter", "Random Adventure",
        "Roll Random Treasure","Check sword for curse","Check Wanted Poster"]
    utils.menu(func_list,desc_list,"Adventure Menu",False)
