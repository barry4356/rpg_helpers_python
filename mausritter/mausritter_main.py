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
import treasure
import custom_terminal

def print_help(args=[]):
    tabwidth=24
    utils.print_header("Help - List of Commands")
    help_list = [
        "Note: You can use [TAB] to auto-complete commands",
        "      You can use [up/down] arrows to use previous commands",
        "",
        "creature\t Create a new random creature",
        "creature [type]\t Create a random instance of specific creature",
        "dmg\t Open enemy damage tracker menu",
        "dmg [creature_name]\t Open enemy damage tracker for specified creature",
        "enctr\t Roll to see if there's a new encounter",
        "enctr -f\t Force an encounter",
        "event\t Open menu to roll a new seasonal event",
        "event [season]\t Roll a new seasonal event for specified season",
        "hex\t Roll a new Map Hex",
        "hex -f\t Roll a new faerie world Map Hex",
        "hex -s\t Roll a new mouse settlement",
        "hide\t Open Hide Something Menu",
        "hide [name] [min] [max]\t Hide object 'name' somewhere between 2 tiles",
        "hide [name] [tile]\t Check for hidden object 'name' at specific spot",
        "nwrm\t Create a new adventure area room",
        "roladv\t Roll a random adventure",
        "rolmaus\t Roll a new Player Character Maus",
        "rolmaus -h [number]\t Roll a Henchman Maus (number to roll multiple)",
        "rolmaus -n [number]\t Roll a Maus NPC (number to roll multiple",
        "roltres\t Roll a random treasure",
        "swchk\t Check a new sword for a curse",
        "wanted\t Check local wanted poster",
        "wanted [num1] [num2]\t Check wanted poster, with min/max tiles",
        "weather\t Check today's weather (opens menu)",
        "weather [season]\t Check today's weather (specify current season)",
        "",
        "help\t Print this list of helpful commands",
        "exit\t Close Terminal"
    ]
    for line in help_list:
        print(line.expandtabs(tabwidth))
    print()

def mausritter_terminal():
    command_list = ["help","rolmaus","enctr","nwrm","dmg",
        "weather","wanted","hex","swchk","roltres",
        "roladv","creature","event","hide"
    ]
    func_list = [print_help,maus_roller.rolmaus,encounters.enctr,dungeon.nwrm,combat.dmg,
        weather.weather,contracts.wanted,hexmap_builder.hex,treasure.swchk,treasure.roltres,
        encounters.roladv, dungeon.creature, weather.event, hide_something.hide
    ]
    custom_terminal.terminal(func_list,command_list,header="maus_terminal")

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

if __name__ == "__main__":
    main_menu()
