#dungeon.py
import utils
import chance_table_dungeon
import dice

def print_combat():
    print()
    print("          )     *                            ")
    print("   (   ( /(   (  `      (     (       *   )  ")
    print("   )\  )\())  )\))(   ( )\    )\    ` )  /(  ")
    print(" (((_)((_)\  ((_)()\  )((_)((((_)(   ( )(_)) ")
    print(" )\___  ((_) (_()((_)((_)_  )\ _ )\ (_(_())  ")
    print("((/ __|/ _ \ |  \/  | | _ ) (_)_\(_)|_   _|  ")
    print(" | (__| (_) || |\/| | | _ \  / _ \    | |    ")
    print("  \___|\___/ |_|  |_| |___/ /_/ \_\   |_|    ")
                                             


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
        print("0 - Main Menu")
        val = utils.get_input()
        if(val == 0):
            exit = True
        elif(val < 11):
            select_enemy(val)
        
def select_enemy(selected_id):

    exit = False;
    while exit != True:
        utils.print_header("")
        print("0 - Main Menu")
        val = utils.get_input()
        if(val == 0):
            exit = True

def track_damage(name,hp,str,dex,wil,arm,atk_str,extra_str,wants_str):
    print ("WIP")

def menu():
    print_combat()
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
