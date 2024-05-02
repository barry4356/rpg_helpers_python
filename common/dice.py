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
    return (random.randint(1,dice_size))

#Roll D3(s)
def roll_1d3():
    return(roll_custom(3))

#Roll D4(s)
def roll_1d4():
    return(roll_custom(4))

#Roll D6(s)
def roll_1d6():
    return (roll_custom(6))
    
def roll_2d6():
    val = roll_1d6() + roll_1d6()
    return (val)
    
def roll_2d6_keep1():
    val1 = roll_1d6()
    val2 = roll_1d6()
    if val1 > val2:
        return val1
    else:
        return val2

def roll_3d6():
    val = roll_1d6() + roll_1d6() + roll_1d6()
    return (val)

def roll_3d6_keep2():
    dice = [0,0,0]
    dice[0] = roll_1d6()
    dice[1] = roll_1d6()
    dice[2] = roll_1d6()
    dice.remove(min(dice))
    return sum(dice)

#Roll D8(s)
def roll_1d8():
    return (roll_custom(8))

def roll_2d8():
    val = roll_1d8() + roll_1d8()
    return (val)

#Roll D10(s)
def roll_1d10():
    return (roll_custom(10))

#Roll D20(s)
def roll_1d20():
    return (roll_custom(20))
    
#Roll on arbitrary-sized table, all chances are equally weighted
def roll_on_table(input_table):
    table_size = len(input_table)
    return(input_table[roll_custom(table_size)-1])

