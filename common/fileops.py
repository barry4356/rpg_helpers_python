#fileops.py
import os

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
