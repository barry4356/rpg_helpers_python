#utils.py

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