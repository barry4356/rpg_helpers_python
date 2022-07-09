#dice.py
import random
import utils

#Flips a coin
def coin_flip():
    if random.randint(0, 1) == 1:
        return True
    else:
        return False

#Rolls a custom-sized die
def roll_custom(dice_size):
    return (random.randrange(dice_size)+1)

#Roll D6(s)
def roll_1d6():
    return (random.randrange(6) + 1)
    
def roll_2d6():
    val = roll_1d6() + roll_1d6()
    return (val)
    
def roll_3d6():
    val = roll_1d6() + roll_1d6() + roll_1d6()
    return (val)

#Roll D8(s)
def roll_1d8():
    return (random.randrange(8) + 1)

def roll_2d8():
    val = roll_1d8() + roll_1d8()
    return (val)

#Roll D10(s)
def roll_1d10():
    return (random.randrange(10) + 1)

#TODO Make this use custom?
def roll_1d15():
    return (random.randrange(15) + 1)

#Roll D20(s)
def roll_1d20():
    return (random.randrange(20) + 1)
    
#Roll on arbitrary-sized table, all values equal chance
def roll_on_table(input_table):
    table_size = len(input_table)
    return(input_table[roll_custom(table_size)-1])


def menu():
    exit = False;
    while exit != True:
        utils.print_header("Dice Roller")
        print("How many dice to roll?")
        print("1 - 1 6-sided Die")
        print("2 - 2 6-sided Dice")
        print("3 - 3 6-sided Dice")
        print("4 - 1 8-sided Die")
        print("5 - 2 8-sided Dice")
        print("6 - 1 15-sided Die")
        print("7 - 1 20-sided Die")
        print("0 - Main Menu")
        val = utils.get_input()
        print()
        if(val == 0):
            exit = True
        elif(val == 1):
            print(roll_1d6())
        elif(val == 2):
            print(roll_2d6())
        elif(val == 3):
            print(roll_3d6())
        elif(val == 4):
            print(roll_1d8())
        elif(val == 5):
            print(roll_2d8())
        elif(val == 6):
            print(roll_1d15())
        elif(val == 7):
            print(roll_1d20())
        print()
