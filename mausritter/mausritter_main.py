#mappa_imperium_helper.py
import utils
import dice
import dungeon
import combat
import maus_roller
import weather
import hexmap_builder
import ascii_art
import hide_something
import table_lookups
import encounters

def print_help(args=[]):
    utils.print_header("Help - List of Commands")
    print("rolmaus : Roll a new Player Character Maus")
    print("rolmaus -h [number] : Roll a new Henchman Maus (optional number to roll multiple)")
    print("rolmaus -n [number] : Roll a new Maus NPC (Optional number to roll multiple")
    print("enctr : Roll to see if there's a new encounter (1d6)")
    print("enctr -f : Force an encounter")
    print("nwrm : Create a new adventure area room")
    print("exit : Close Terminal")
    print()

def mausritter_terminal():
    command_list = ["help","rolmaus","enctr","nwrm"]
    func_list = [print_help,maus_roller.rolmaus,encounters.enctr,dungeon.nwrm]
    utils.terminal(func_list,command_list,header="maus_terminal")

def main_menu():
    ascii_art.print_mausritter()
    func_list = [
        dungeon.menu, combat.menu, maus_roller.menu, 
        weather.menu, hexmap_builder.menu, hide_something.menu,
        table_lookups.menu,mausritter_terminal
    ]
    desc_list = [
        "Adventure Utils", "Combat Helper", "Maus Creator", 
        "Weather Utils", "Hexmap Builder", "Hide Something",
        "Lookup Table","Mausritter Terminal"
    ]
    utils.menu(func_list,desc_list,"MAUSRITTER HELPER",True)

main_menu()
