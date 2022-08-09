#pyDungeon_fileops.py

import fileops

def store_map(my_map):
    print("store_map")
    for room in my_map.rooms:
        store_room(room)
    for node in my_map.nodes:
        store_node(node)

def store_room(my_room):
    print("store_room")

def store_node(my_node):
    print("store_node")

def read_map(map_file):
    print("read_map")

def read_room(room_file):
    print("read_room")

def read_node(node_file):
    print("read_node")