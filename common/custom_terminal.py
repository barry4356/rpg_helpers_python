#custom_terminal.py

import readline

class MyCompleter(object):  # Custom completer
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

def get_input_terminal(default="",header="terminal"):
    val = default
    try:
        val = input(header+"> ")
    except ValueError:
        print("Invalid")
    return str(val)

def terminal(func_list,command_list,header="terminal"):
    completer = MyCompleter(command_list)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    if len(func_list) != len(command_list):
        print("ERROR: terminal needs two lists of same size!!")
        return
    last_command = ""
    exit_terminal = False
    while exit_terminal != True:
        val = get_input_terminal(header=header)
        if(val.lower() == "exit"):
            exit_terminal = True
        else:
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