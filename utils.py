#utils.py

def print_header(title):
    print()
    print()
    print("=============== " + title + " ===============")
    print()
    
def get_input():
    val = "INVALID"
    try:
        val = float(input("Enter Selection: "))
    except ValueError:
        print("Invalid")
    return val
