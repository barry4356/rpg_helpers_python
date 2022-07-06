#dice.py
import random

def roll_1d6():
    return (random.randrange(6) + 1)
    
def roll_2d6():
    val = roll_1d6() + roll_1d6()
    return (val)
    
def roll_3d6():
    val = roll_1d6() + roll_1d6() + roll_1d6()
    return (val)

def roll_1d8():
    return (random.randrange(8) + 1)

def roll_2d8():
    val = roll_1d8() + roll_1d8()
    return (val)

def roll_1d15():
    return (random.randrange(15) + 1)

def roll_1d20():
    return (random.randrange(20) + 1)
