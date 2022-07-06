#mappa_imperium_helper.py
import dice
import utils
import dungeon
        
def dice_menu():
    exit = False;
    while exit != True:
        utils.print_header("Dice Roller")
        print("How many dice to roll?")
        print("1 - 1 6-sided Die")
        print("2 - 2 6-sided Dice")
        print("3 - 3 6-sided Dice")
        print("0 - Main Menu")
        val = utils.get_input()
        print()
        if(val == 0):
            exit = True
        elif(val == 1):
            print(dice.roll_1d6())
        elif(val == 2):
            print(dice.roll_2d6())
        elif(val == 3):
            print(dice.roll_3d6())
        print()

exit = False;
while exit != True:
    print ("\n===== MAUSRITTER HELPER =====\n")
    print("Menu Selection...")

    print("1 - Adventure Site Utils")
    print("2 - Roll Dice")
    print("0 - Exit")
    
    val = utils.get_input()
    print("\n")
    
    if(val == 0):
        exit = True
    elif (val == 1):
        print(dungeon.menu())
    elif (val == 2):
        dice_menu()
