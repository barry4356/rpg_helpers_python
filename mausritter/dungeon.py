#dungeon.py
import utils
import chance_table_dungeon
import dice

def create_dungeon_room():
    utils.print_header("Room")
    room_type = chance_table_dungeon.room_type[dice.roll_1d6()-1]
    print ("Room Type: " + room_type)

def menu():
    exit = False;
    while exit != True:
        utils.print_header("Adventure-Site Menu")
        print("1 - Create New Room")
        print("0 - Main Menu")
        val = utils.get_input()
        if(val == 0):
            exit = True
        elif(val == 1):
            create_dungeon_room()
