#dungeon.py
import utils
import chance_table_dungeon
import dice
import enemy_stats_tables
import ascii_art

def begin_damage_tracking():
    exit = False;
    while exit != True:
        utils.print_header("Choose Enemy")
        print("What Creature are we doing damage to?")
        print("1  - Centipede")
        print("2  - Crow")
        print("3  - Frog")
        print("4  - Faerie")
        print("5  - Ghost")
        print("6  - Mouse")
        print("7  - Owl")
        print("8  - Snake")
        print("9  - Rat")
        print("10 - Spider")
        print("0 - Back")
        val = utils.get_input()
        if(val == 0):
            exit = True
        elif(val < 11):
            select_enemy(val)
        
def select_enemy(selected_id):
    name = ""
    stats = []
    if selected_id == 1:
        name = "Centipede"
        stats = enemy_stats_tables.centipede_stats
    elif selected_id == 2:
        name = "Crow"
        stats = enemy_stats_tables.crow_stats
    elif selected_id == 3:
        name = "Frog"
        stats = enemy_stats_tables.frog_stats
    elif selected_id == 4:
        name = "Faerie"
        stats = enemy_stats_tables.faerie_stats
    elif selected_id == 5:
        name = "Ghost"
        stats = enemy_stats_tables.ghost_stats
    elif selected_id == 6:
        name = "Mouse"
        stats = enemy_stats_tables.mouse_stats
    elif selected_id == 7:
        name = "Owl"
        stats = enemy_stats_tables.owl_stats
    elif selected_id == 8:
        name = "Snake"
        stats = enemy_stats_tables.snake_stats
    elif selected_id == 9:
        name = "Rat"
        stats = enemy_stats_tables.rat_stats
    else:
        name = "Spider"
        stats = enemy_stats_tables.spider_stats

    track_damage(name,stats[0],stats[1],stats[2],stats[3],stats[4],
        stats[5],stats[6])

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
    exit = False;
    while exit != True:
        utils.print_header("Combat Menu")
        print("1 - Enemy Damage Tracker")
        print("0 - Main Menu")
        val = utils.get_input()
        if(val == 0):
            exit = True
        elif(val == 1):
            begin_damage_tracking()
