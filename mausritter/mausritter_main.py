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
import contracts

def print_help(args=[]):
    tabwidth=22
    utils.print_header("Help - List of Commands")
    help_list = [
        "dmg\t Open enemy damage tracker menu",
        "dmg [creature_name]\t Open enemy damage tracker for specified creature",
        "enctr\t Roll to see if there's a new encounter",
        "enctr -f\t Force an encounter",
        "nwrm\t Create a new adventure area room",
        "rolmaus\t Roll a new Player Character Maus",
        "rolmaus -h [number]\t Roll a new Henchman Maus (number to roll multiple)",
        "rolmaus -n [number]\t Roll a new Maus NPC (number to roll multiple",
        "wanted\t Check local wanted poster",
        "wanted [num1] [num2]\t Check wanted poster, w/ min/max tiles",
        "weather\t Check today's weather (opens menu)",
        "weather [season]\t Check today's weather (specify current season)",
        "",
        "exit\t Close Terminal"
    ]
    for line in help_list:
        print(line.expandtabs(tabwidth))
    print()

def mausritter_terminal():
    command_list = ["help","rolmaus","enctr","nwrm","dmg",
        "weather","wanted"]
    func_list = [print_help,maus_roller.rolmaus,encounters.enctr,dungeon.nwrm,combat.dmg,
        weather.weather,contracts.wanted]
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
