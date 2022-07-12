#mappa_imperium_helper.py
import utils
import dice
import dungeon
import combat
import maus_roller
import weather
import encounters
import hexmap_builder

def print_logo():
    print("  __  __                      _ _   _            ")
    print(" |  \/  | __ _ _   _ ___ _ __(_) |_| |_ ___ _ __ ")
    print(" | |\/| |/ _` | | | / __| '__| | __| __/ _ \ '__|")
    print(" | |  | | (_| | |_| \__ \ |  | | |_| ||  __/ |   ")
    print(" |_|  |_|\__,_|\__,_|___/_|  |_|\__|\__\___|_|   ")
    print("")


def main_menu():
    print_logo()
    func_list = [dungeon.menu,combat.menu,maus_roller.menu,weather.menu,hexmap_builder.menu]
    desc_list = ["Adventure Utils","Combat Helper","Maus Creator","Weather Utils","Hexmap Builder"]
    utils.menu(func_list,desc_list,"MAUSRITTER HELPER",True)

main_menu()
