#pyDungeon_fileops.py

import fileops
import os
from pyDungeon_classes import Map
from pyDungeon_classes import Room
from pyDungeon_classes import Node
import numpy as np

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
    read_map(savelocation+my_map.map_name.replace(" ","_")+".map") #TEST CODE

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
        matrix_dict[str(index)] = line.tolist()
        index = index + 1
    fileops.serialize_dict(matrix_dict,filename)

def read_map(map_file):
    map_dict = fileops.deserialize_dict(map_file)
    my_map = Map(map_width=map_dict["map_width"],map_height=map_dict["map_height"],map_name=map_dict["map_name"])
    #Convert string into a set of two ints (x,y coordinates)
    my_map.player_location = list(map(int,map_dict["PC_location"].split(",")))
    savelocation = os.path.dirname(map_file)+"/"
    my_map.matrix = read_matrix(savelocation+my_map.map_name.replace(" ","_")+".matrix",my_map.map_width,my_map.map_height)
    my_map.mask_matrix = read_matrix(savelocation+my_map.map_name.replace(" ","_")+".mask",my_map.map_width,my_map.map_height)
    for key in map_dict.keys():
        if "room" in key:
            my_map.rooms.append(read_room(savelocation+key+".room"))
        if "node" in key:
            my_map.nodes.append(read_node(savelocation+key+".node"))
    return my_map

def read_room(room_file):
    room_dict = fileops.deserialize_dict(room_file)
    my_room = Room(x=room_dict["x"],y=room_dict["y"],width=room_dict["width"],height=room_dict["height"])
    my_room.room_number = room_dict["room_number"]
    for key in room_dict.keys():
        if "node" in key:
            my_room.nodes.append(room_dict[key])
    for key in room_dict.keys():
        if "description" in key:
            my_room.description.append(room_dict[key])
    return my_room

def read_node(node_file):
    node_dict = fileops.deserialize_dict(node_file)
    my_node = Node(x=node_dict["x"],y=node_dict["y"],label=node_dict["label"])
    my_node.room = node_dict["room"]
    for key in node_dict.keys():
        if "connection" in key:
            my_node.connections.append(node_dict[key])
    return my_node

def read_matrix(matrix_file,map_width,map_height):
    s = (map_height,map_width)
    my_matrix = np.zeros(s)
    matrix_dict = fileops.deserialize_dict(matrix_file)
    y = 0
    for key in matrix_dict.keys():
        x = 0
        for value in matrix_dict[key].split(","):
            value = value.replace("[","")
            value = value.replace("]","")
            my_matrix[y][x] = int(float(value))
            x = x + 1
        y = y + 1
    return my_matrix