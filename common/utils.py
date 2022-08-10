#utils.py

def array_select_menu(array=[],header="",is_main=False):
    exit = False
    while exit != True:
        print_header(header)
        print("Input Selection...")
        index=0
        for option in array:
            index=index+1
            print(str(index)+" - "+option)
        if is_main:
            print("\n0 - Exit")
        else:
            print("0 - Back")
        val = get_input_int(100)
        print("\n")
        if(val == 0):
            return ""
        elif val <= len(array):
            return(array[val-1])

def round(number_input):
    number_int = int(number_input)
    remainder = number_input - float(number_int)
    if remainder >= 0.5:
        number_int = number_int + 1
    return int(number_int)

def sqrt(input_num):
    return input_num**(1/2)

def areyousure():
    exit = False;
    while exit != True:
        print("Are you Sure you want to Exit the program?")
        print("1 - YES")
        print("0 - NO")
        val = get_input()
        print("\n")
        if(val == 1):
            return True
        else:
            return False

def print_header(title):
    print()
    print()
    print("=============== " + title + " ===============")
    print()
    
def get_input(default=0.0):
    val = default
    print()
    try:
        val = float(input("Enter Selection: "))
    except ValueError:
        print("Invalid")
    print()
    return val

def to_int(input_val):
    return_val = 0
    try:
        return_val = int(input_val)
    except ValueError:
        print("Invalid Input")
    return return_val

def get_input_int(default=0):
    val = default
    print()
    try:
        val = int(input("Enter Selection: "))
    except ValueError:
        print("Invalid")
    print()
    return val

def get_input_str(default=""):
    val = default
    print()
    try:
        val = input("Enter Selection: ")
    except ValueError:
        print("Invalid")
    print()
    return val

def wait4enter():
    print()
    input("Press Enter to continue...")

def menu(func_list,desc_list,header,is_main):
    if len(func_list) != len(desc_list):
        print("ERROR: utils.menu needs two lists of same size!!")
        return
    exit = False
    while exit != True:
        print_header(header)
        print("Menu Selection...")
        index=0
        for desc in desc_list:
            index=index+1
            print(str(index)+" - "+desc)
        if is_main:
            print("0 - Exit")
        else:
            print("0 - Back")
        val = get_input_int(100)
        print("\n")
        if(val == 0):
            if is_main:
                if areyousure():
                    exit = True
            else:
                exit = True
        elif val <= len(func_list):
            func_list[val-1]()
