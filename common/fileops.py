#fileops.py
import os

#Write out a dict to a file
def serialize_dict(input_dict,output_file):
    separator="->"
    serialized_str=""
    for key, value in input_dict.items():
        serialized_str = (serialized_str+key+separator+str(value)+"\n")
    write_file(output_file,serialized_str)

#Read a dict in from a file
def deserialize_dict(input_file):
    separator="->"
    deserialized_dict={}
    raw_string = read_file(input_file)
    raw_string = raw_string.split("\n")
    for my_string in raw_string:
        my_string = my_string.split(separator)
        if len(my_string) != 2:
            break
        deserialized_dict[my_string[0]] = my_string[1]
    return deserialized_dict

def get_files(suffix="", path=""):
    returnfiles = []
    try:
        onlyfiles = os.listdir(path)
    except FileNotFoundError:
        print ("ERROR: No such directory ["+path+"]")
        return returnfiles
    for myfile in onlyfiles:
        if suffix in myfile:
            returnfiles.append(myfile)
    return returnfiles

def remove_file(my_filename):
    if os.path.exists(my_filename):
        os.remove(my_filename)
    else:
        print("ERROR: Failed to Remove file "+str(my_filename))

def mkdir_file(filename=""):
    if not filename:
        print("ERROR: NULL Filename")
    file_dir = os.path.dirname(os.path.abspath(filename))
    isExist = os.path.exists(file_dir)
    if not isExist:
        os.makedirs(file_dir)

def write_file(my_filename,my_filecontent):
    mkdir_file(filename=my_filename)
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
