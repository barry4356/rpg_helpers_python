#table_lookups.py
import utils
import lookup_tables

def table_menu(table_name_list,table_list):
    exit = False
    while exit != True:
        utils.print_header("Lookup a Table")
        print("Table Selection...")
        index=0
        for table_name in table_name_list:
            index=index+1
            print(str(index)+" - "+table_name)
        print("0 - Back")
        val = utils.get_input_int(100)
        print("\n")
        if(val == 0):
            exit = True
        elif val <= len(table_list):
            print_table(table_list[val-1])

def weather_menu():
    table_menu(lookup_tables.weather_table_name_list,
        lookup_tables.weather_table_list)

def magic_menu():
    table_menu(lookup_tables.magic_table_name_list,
        lookup_tables.magic_table_list)

def print_table(table):
    index = 0
    for entry in table:
        index = index + 1
        print(str(index)+"\t"+str(entry))

def menu():
    func_list = [weather_menu,magic_menu]
    desc_list = ["Weather Tables","Magic Tables"]
    utils.menu(func_list,desc_list,"Table Lookup",False)