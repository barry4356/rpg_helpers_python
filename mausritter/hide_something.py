#hide_something.py
import utils
import random

def hide_something():
    exit = False
    while exit != True:
        print("What do we want to call this object?")
        val = utils.get_input_str()
        print("\n")
        if(val != ""):
            object_name = val
            exit = True
    exit = False
    while exit != True:
        print("What is the lower bound of the tile this can be in?")
        val = utils.get_input_int(-1)
        minval = val
        print("\n")
        if(val != -1):
            print("What is the upper bound of the tile this can be in?")
            val = utils.get_input(-1)
            maxval = val
            if minval >= maxval:
                print("Lower bound must be less than upper bound!\n")
            else:
                exit = True
    hidden_location = random.randint(minval,maxval)
    f = open("mausritter/data/"+object_name+".maus", "w")
    f.write(str(hidden_location))
    f.close

def menu():
    func_list=[hide_something]
    desc_list=["Hide Something"]
    utils.menu(func_list,desc_list,"Hide Something in Random Tile",False)
