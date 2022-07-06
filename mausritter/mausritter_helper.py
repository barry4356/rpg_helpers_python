#mappa_imperium_helper.py
import dice
import utils
import dungeon
import combat

def main_menu():     
    exit = False;
    while exit != True:
        utils.print_header("MAUSRITTER HELPER")
        print("Menu Selection...")

        print("1 - Adventure Site Utils")
        print("2 - Combat Helper")
        print("0 - Exit")
    
        val = utils.get_input()
        print("\n")
    
        if(val == 0):
            if utils.areyousure():
                exit = True
        elif (val == 1):
            print(dungeon.menu())
        elif (val == 2):
            print(combat.menu())

main_menu()