#pyDungeon_fileops.py

import fileops

def store_map(my_map,savelocation="maps/"):
    map_dict = {}
    savelocation = savelocation + my_map.map_name.replace(" ","_")+"/"
    map_dict["map_name"]=my_map.map_name
    map_dict["map_width"]=my_map.map_width
    map_dict["map_height"]=my_map.map_height
    map_dict["PC_location"]=str(my_map.player_location[0])+","+str(my_map.player_location[1])
    for room in my_map.rooms:
        room_filename = "room"+str(room.room_number)+".room"
        map_dict["room"+str(room.room_number)] = room_filename
        store_room(room,savelocation+room_filename)
    for node in my_map.nodes:
        node_filename = "node"+str(node.label)+".node"
        map_dict["node"+str(node.label)] = node_filename
        store_node(node,savelocation+node_filename)
    map_matrix_filename = my_map.map_name.replace(" ","_")+".matrix"
    map_dict["matrix"]=map_matrix_filename
    store_matrix(my_map.matrix,savelocation+map_matrix_filename)
    mask_matrix_filename = my_map.map_name.replace(" ","_")+".mask"
    map_dict["mask_matrix"]=mask_matrix_filename
    store_matrix(my_map.mask_matrix,savelocation+mask_matrix_filename)
    fileops.serialize_dict(map_dict,savelocation+my_map.map_name.replace(" ","_")+".map")

def store_room(my_room,filename):
    room_dict = {}
    room_dict["x"] = my_room.x
    room_dict["y"] = my_room.y
    room_dict["width"] = my_room.width
    room_dict["height"] = my_room.height
    room_dict["room_number"] = my_room.room_number
    line_index = 0
    for line in my_room.description:
        room_dict["line"+str(line_index)] = line
        line_index = line_index + 1
    node_index = 0
    for node in my_room.nodes:
        room_dict["node"+str(node_index)] = node
        node_index = node_index + 1
    fileops.serialize_dict(room_dict,filename)

def store_node(my_node,filename):
    node_dict = {}
    node_dict["x"] = my_node.x
    node_dict["y"] = my_node.y
    node_dict["label"] = my_node.label
    node_dict["room"] = my_node.room
    connection_index = 0
    for connection in my_node.connections:
        node_dict["connection"+str(connection_index)] = connection
        connection_index = connection_index + 1
    fileops.serialize_dict(node_dict,filename)

def store_matrix(my_matrix,filename):
    matrix_dict = {}
    index = 0
    for line in my_matrix:
        matrix_dict[str(index)] = line
        index = index + 1
    fileops.serialize_dict(matrix_dict,filename)

def read_map(map_file):
    print("read_map")

def read_room(room_file):
    print("read_room")

def read_node(node_file):
    print("read_node")

def read_matrix(matrix_file):
    print("read_matrix")