#dungeon.py
import utils
import dungeon_tables
import creature_tables
import dice
import additional_tables
import encounters
import contracts
import treasure
import treasure_tables

def print_dungeon_room():
    utils.print_header("Room")
    text_array = create_dungeon_room()
    for line in text_array:
        if "list" in str(type(line)):
            for subline in line:
                print(subline)
        else:
            print(line)

def create_dungeon_room():
    text_array = []
    utils.print_header("Room")
    room_type = dice.roll_1d6() - 1
    room_type_str = dungeon_tables.room_type[room_type]
    creature_present = dungeon_tables.creature_present[room_type][dice.roll_1d6()-1]
    treasure_present = dungeon_tables.treasure_present[room_type][dice.roll_1d6()-1]
    text_array.append("Room Type: " + room_type_str)
    if room_type_str == "Empty":
        text_array.append("\tEmpty Detail: " + dungeon_tables.empty_feature[dice.roll_1d20()-1])
    if room_type_str == "Obstacle":
        text_array.append("\tObstacle Detail: " + dungeon_tables.obstacle_feature[dice.roll_1d8()-1])
    if room_type_str == "Trap":
        text_array.append("\tTrap Detail: " + dungeon_tables.trap_feature[dice.roll_1d8()-1])
        if treasure_present:
            text_array.append("\tTRAP HAS TREASURE!!")
            text_array.append(treasure.roll_treasure(tabs=2))
    if room_type_str == "Puzzle":
        puzzle_feature_number = dice.roll_1d6()-1
        puzzle_detail = dungeon_tables.puzzle_feature[puzzle_feature_number]
        text_array.append("\tPuzzle Detail: " + puzzle_detail)
        if "treasure" in puzzle_detail.lower() or "sword" in puzzle_detail.lower() :
            text_array.append("\tPUZZLE HAS TREASURE!!")
            if "sword" in puzzle_detail.lower():
                treasure_type_index = 0
            else:
                treasure_type_index = dice.roll_1d20() - 1
            text_array.append(treasure.roll_treasure(treasure_type=treasure_type_index,tabs=2))
    if room_type_str == "Lair":
        text_array.append("\tLair Detail: " + dungeon_tables.lair_feature[dice.roll_1d6()-1])
    text_array.append("-")
    text_array.append("Creature Present: " + str(creature_present))
    if creature_present:
        is_dangerous,text_array_temp = encounters.roll_encounter(tabs=1,is_dungeon_room=True)
        text_array.append(text_array_temp)
        if is_dangerous and treasure_present:
            text_array.append("\tCREATURE IS GUARDING TREASURE!!")
            text_array.append(treasure.roll_treasure(tabs=2))
    text_array.append("-")
    text_array.append("Treasure Present: " + str(treasure_present))
    if treasure_present:
        text_array.append(treasure.roll_treasure(tabs=1))
        text_array.append(treasure.roll_treasure(tabs=1))
    return text_array

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
    print("Communication: "+str(detail_ary[6]))
    print ("")

def roll_creature_menu(creature="",oneoff=False):
    header = "Roll a Creature"
    if creature not in creature_tables.creatures:
        creature = utils.array_select_menu(array=creature_tables.creatures,header=header)
    if not creature:
        return
    print(creature+" Stats")
    print_stats(creature_tables.enemy_stats[creature])
    print_creature_detail(creature)
    if not oneoff:
        roll_creature_menu()

def menu():
    func_list = [create_dungeon_room, encounters.check_encounter, encounters.adventure_generator,
        treasure.roll_treasure,treasure.check_magic_sword,contracts.print_contract]
    desc_list = ["Create New Room","Roll for Encounter", "Random Adventure",
        "Roll Random Treasure","Check sword for curse","Check Wanted Poster"]
    utils.menu(func_list,desc_list,"Adventure Menu",False)

def nwrm(argv=[]):
    print_dungeon_room()
    print()

def creature(argv=[]):
    if len(argv) == 0:
        roll_creature_menu()
    else:
        roll_creature_menu(argv[0],oneoff=True)
    print()