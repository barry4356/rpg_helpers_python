#utils.py
import os
import readline

class MyCompleter(object):  # Custom completer

    previous_commands = []
    command_index = 0

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try: 
            return self.matches[state]
        except IndexError:
            return None
    
    def push_command(my_command):
        previous_commands.insert(0,my_command)

    def reset_index():
        command_index = 0

    def up_arrow():
        if previous_commands:
            command_index = command_index + 1
            return previous_commands[command_index - 1]

def array_select_menu(array=[],header=""):
    exit = False
    while exit != True:
        print_header(header)
        print("Input Selection...")
        index=0
        for option in array:
            index=index+1
            print(str(index)+" - "+option)
        print("0 - Back")
        val = get_input_int(100)
        print("\n")
        if(val == 0):
            return ""
        elif val <= len(array):
            return(array[val-1])

def get_files(suffix="", path=""):
    onlyfiles = os.listdir(path)
    returnfiles = []
    for myfile in onlyfiles:
        if suffix in myfile:
            returnfiles.append(myfile)
    return returnfiles

def remove_file(my_filename):
    if os.path.exists(my_filename):
        os.remove(my_filename)
    else:
        print("ERROR: Failed to Remove file "+str(my_filename))

def write_file(my_filename,my_filecontent):
    try:
        with open(my_filename,'w') as file:
            file.write(str(my_filecontent))
    except IOError:
        print("ERROR: Failed to write file "+my_filename)

def read_file(my_filename):
    return_string = ""
    try:
        with open(my_filename,'r') as file:
            return_string = file.read()
    except IOError:
        print("ERROR: Failed to read file "+my_filename)
    return return_string

def round(number_input):
    number_int = int(number_input)
    remainder = number_input - float(number_int)
    if remainder >= 0.5:
        number_int = number_int + 1
    return int(number_int)

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
    
def get_input_int(default=0):
    val = default
    print()
    try:
        val = int(input("Enter Selection: "))
    except ValueError:
        print("Invalid")
    print()
    return val

def get_input_terminal(default="",header="terminal"):
    val = default
    try:
        val = input(header+"> ")
    except ValueError:
        print("Invalid")
    return str(val)

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

def terminal(func_list,command_list,header="terminal"):
    completer = MyCompleter(command_list)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    #readline.parse_and_bind('"\\e[A": up_arrow')
    #readline.parse_and_bind('tab: up_arrow')
    if len(func_list) != len(command_list):
        print("ERROR: utils.terminal needs two lists of same size!!")
        return
    last_command = ""
    exit_terminal = False
    while exit_terminal != True:
        val = get_input_terminal(header=header)
        if(val.lower() == "exit"):
            exit_terminal = True
        else:
            if(val.lower() == "p"):
                val = last_command
                print(header+"> "+last_command)
            process_terminal_input(func_list=func_list,command_list=command_list,input_val=val.lower())
            last_command = val.lower()

def process_terminal_input(func_list,command_list,input_val=""):
    input_arr = input_val.split(' ')
    command = input_arr[0]
    input_arr.pop(0)
    args = input_arr
    index = 0
    index_selected = -1
    for command_entry in command_list:
        if command == command_entry:
            index_selected = index
            break
        index = index + 1
    if index_selected >= 0:
        func_list[index_selected](args)
