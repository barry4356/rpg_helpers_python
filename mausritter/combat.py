#dungeon.py
import utils
import chance_table_dungeon
import dice
import creature_tables
import ascii_art
import dungeon

def begin_damage_tracking():
    creature = utils.array_select_menu(array=creature_tables.creatures, header="Choose Enemy")
    stats = get_stats(creature)
    track_damage(creature,stats[0],stats[1],stats[2],stats[3],stats[4],
        stats[5],stats[6])

def get_stats(creature_name):
    return (creature_tables.enemy_stats[creature_name])

def track_damage(name,hp,strength,dex,wil,arm,atk_str,wants_str):
    exit = False;
    while exit != True:
        utils.print_header(name)
        print("HP: "+str(hp)+" STR: "+str(strength)+" DEX: "+str(dex)
            +" WIL: "+str(wil)+" Armor: "+str(arm))
        print("Attack: "+atk_str)
        print(wants_str)
        if strength == 0:
            print("\nENEMY IS DEAD!!")
        elif hp == 0:
            print("\nENEMY NEEDS TO MAKE A STRENGTH SAVE")
        print("\nHow much damage did we do (before armor)??")
        print("0 - Back")
        val = utils.get_input(0.1)
        if val == 0:
            if strength == 0:
                ascii_art.printdeath()
                print("Well Struck!")
            exit = True
        else:
            hp,strength = do_damage(hp,strength,arm,val)

def do_damage(hp,strength,arm,dam):
    dam=round(dam)
    if dam < arm:
        dam = 0
        print("Armor prevented damage!")
    elif arm > 0:
        dam = int(dam - arm)
        print("Armor blocks ["+str(arm)+"], New Damage ["+str(dam)+"]")
    if hp > dam:
        hp = hp - dam
    elif dam == hp:
        hp = 0
    else:
        dam = dam - hp
        hp = 0
        strength = strength - dam
        if strength < 0:
            strength = 0
    return int(hp),int(strength)

def menu():
    ascii_art.print_combat()
    func_list = [begin_damage_tracking,dungeon.roll_creature_menu]
    desc_list = ["Enemy Damage Tracker","Roll New Creature"]
    utils.menu(func_list,desc_list,"Combat Menu",False)

