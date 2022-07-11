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
    
#Roll on arbitrary-sized table, all chances are equally weighted
def roll_on_table(input_table):
    table_size = len(input_table)
    return(input_table[roll_custom(table_size)-1])

