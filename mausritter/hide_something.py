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
    utils.write_file("mausritter/data/"+object_name+".hidden",hidden_location)

def check_for_object():
    utils.print_header("Look for Object")
    hidden_object_filenames = utils.get_files(path="./mausritter/data/",suffix=".hidden")
    hidden_objects = list({x.replace('.hidden','') for x in hidden_object_filenames})
    exit = False
    while exit != True:
        object_index = 0
        for my_object in hidden_objects:
            object_index = object_index+1
            print(str(object_index)+" - "+my_object)
        print("\n0 - Back")
        print("which item are we looking for?")
        val = utils.get_input_int()
        print("\n")
        if val == 0:
            exit = True
        elif val <= len(hidden_objects):
            check_tile(hidden_objects[val-1])
        else:
            print("INVALID")

def check_tile(my_object):
    tile = utils.read_file("mausritter/data/"+my_object+".hidden")
    exit = False
    while exit != True:
        print("What tile are you looking in for the "+my_object+"?")
        print("0 - Back")
        val = str(utils.get_input_int())
        print("\n")
        if val == tile:
            print("YOU FOUND THE "+my_object+"!!\n")
        elif val == "0":
            exit = True
        else:
            print("You haven't found the "+my_object)

def delete_object():
    utils.print_header("Delete Hidden Object")
    exit = False
    while exit != True:
        hidden_object_filenames = utils.get_files(path="./mausritter/data/",suffix=".hidden")
        hidden_objects = list({x.replace('.hidden','') for x in hidden_object_filenames})
        object_index = 0
        for my_object in hidden_objects:
            object_index = object_index+1
            print(str(object_index)+" - "+my_object)
        print("\n0 - Back")
        print("which object are we deleting?")
        val = utils.get_input_int()
        print("\n")
        if val == 0:
            exit = True
        elif val <= len(hidden_objects):
            utils.remove_file("mausritter/data/"+hidden_objects[val-1]+".hidden")
        else:
            print("INVALID INPUT")

def menu():
    func_list=[hide_something,check_for_object,delete_object]
    desc_list=["Hide Something","Check if I found it","Delete a hidden object"]
    utils.menu(func_list,desc_list,"Hide Something in Random Tile",False)

def hide(argv=[]):
    if len(argv) == 0:
        menu()
    else:
        menu()
    print()