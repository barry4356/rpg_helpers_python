#pyDungeon_fileops.py

import fileops

def store_map(my_map):
    map_dict = {}
    map_dict["map_name"]=my_map.map_name
    map_dict["map_width"]=my_map.map_width
    map_dict["map_height"]=my_map.map_height
    map_dict["PC_location"]=str(my_map.player_location[0])+","+str(my_map.player_location[1])
    for room in my_map.rooms:
        map_dict["room"+str(room.room_number)] = ("room"str(room.room_number)".room")
        store_room(room)
    for node in my_map.nodes:
        map_dict["node"+str(node.label)] = ("node"str(node.label)".node")
        store_node(node)
    map_dict["matrix"]=my_map.map_name+".matrix"
    store_matrix(my_map.matrix)
    map_dict["mask_matrix"]=my_map.map_name+".mask"
    store_matrix(my_map.mask_matrix)
    fileops.serialize_dict(map_dict,"maps/"+my_map.map_name+"/"+my_map.map_name+".map")

def store_room(my_room):
    print("store_room")

def store_node(my_node):
    print("store_node")

def store_matrix(my_matrix):
    print("store_matrix")

def read_map(map_file):
    print("read_map")

def read_room(room_file):
    print("read_room")

def read_node(node_file):
    print("read_node")

def read_matrix(matrix_file):
    print("read_matrix")