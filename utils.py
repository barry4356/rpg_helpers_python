#utils.py

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
    
def get_input():
    val = "INVALID"
    print()
    try:
        val = float(input("Enter Selection: "))
    except ValueError:
        print("Invalid")
    print()
    return val

def wait4enter():
    print()
    input("Press Enter to continue...")