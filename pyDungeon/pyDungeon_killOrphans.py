#pyDungeon_killOrphans.py
from pyDungeon_utils import find_node
from pyDungeon_utils import find_room

def kill_orphans(my_map,start_label="start"):
    # Find list of all rooms
    room_list = set([])
    rooms_discovered_set = set([])
    for room in my_map.rooms:
        room_list.add(room.room_number)
    print (room_list)
    # Travel each node from the start
    node_list = set([])
    node_list.add(start_label)
    #node_list.append(find_node(my_map.nodes,start_label))
    #Max iterations 1000... shouldn't come to that
    for i in range(1000):
        rooms_discovered_set, node_list_new = walk_nodes(my_map,node_list)
        if node_list_new == node_list:
            break
        #print(node_list)
        print(node_list_new)
        node_list = node_list_new
    print (rooms_discovered_set)
    # Log how many rooms are explored
    # Find list of Rooms that are orphaned
    # Create a connection from each orphaned to a nearby non-orphan
    return my_map

def walk_nodes(my_map,node_list):
    rooms_set = set([])
    node_list_out = node_list.copy()
    for node_name in node_list:
        actual_node = find_node(my_map.nodes,node_name)
        if actual_node:
            for connection in actual_node.connections:
                if "list" in str(type(connection)):
                    node_list_out.add(connection[0])
                else:
                    node_list_out.add(connection)
            actual_room = find_room(my_map.rooms,actual_node.room)
            if actual_room:
                rooms_set.add(actual_room.room_number)
                for node in actual_room.nodes:
                    node_list_out.add(node)
    return rooms_set,node_list_out
