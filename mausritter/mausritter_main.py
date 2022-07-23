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
    tabwidth=22
    utils.print_header("Help - List of Commands")
    print("dmg\t Open enemy damage tracker menu".expandtabs(tabwidth))
    print("dmg [creature_name]\t Open enemy damage tracker for specified creature".expandtabs(tabwidth))
    print("enctr\t Roll to see if there's a new encounter".expandtabs(tabwidth))
    print("enctr -f\t Force an encounter".expandtabs(tabwidth))
    print("nwrm\t Create a new adventure area room".expandtabs(tabwidth))
    print("rolmaus\t Roll a new Player Character Maus".expandtabs(tabwidth))
    print("rolmaus -h [number]\t Roll a new Henchman Maus (number to roll multiple)".expandtabs(tabwidth))
    print("rolmaus -n [number]\t Roll a new Maus NPC (number to roll multiple".expandtabs(tabwidth))
    print()
    print("exit\t Close Terminal".expandtabs(tabwidth))
    print()

def mausritter_terminal():
    command_list = ["help","rolmaus","enctr","nwrm","dmg"]
    func_list = [print_help,maus_roller.rolmaus,encounters.enctr,dungeon.nwrm,combat.dmg]
    utils.terminal(func_list,command_list,header="maus_terminal")

def main_menu():
    ascii_art.print_mausritter()
    func_list = [
        dungeon.menu, combat.menu, maus_roller.menu, 
        weather.menu, hexmap_builder.menu, hide_something.menu,
        mausritter_terminal
    ]
    desc_list = [
        "Adventure Utils", "Combat Helper", "Maus Creator", 
        "Weather Utils", "Hexmap Builder", "Hide Something",
        "Mausritter Terminal"
    ]
    utils.menu(func_list,desc_list,"MAUSRITTER HELPER",True)

main_menu()
