#dungeon.py
import utils

def menu():
    exit = False;
    while exit != True:
        utils.print_header("Main Menu")
        print("0 - Main Menu")
        val = utils.get_input()
        if(val == 0):
            exit = True
