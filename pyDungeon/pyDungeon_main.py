import random
import numpy as np
from pyDungeon_utils import check_room_overlap
from pyDungeon_utils import sort_rooms_x
from pyDungeon_utils import sort_rooms_y
from pyDungeon_utils import draw_dungeon
from pyDungeon_classes import Room
from pyDungeon_classes import Node
from pyDungeon_classes import Map

map_width = 60 # number of squares wide
map_height = 60 # number of squares tall

min_room_size = 4
max_room_size = 15
max_rooms = 14
min_rooms = 12
max_iters = 3
rooms = []
my_map = []
my_mask = []
my_nodex = []
node_label = 'a'
nodes = []
pc_point = [0,0]

def init_map():
    """Initializes the map of key/value pairs."""
    global my_map
    global my_mask
    s = (map_height,map_width)
    my_map = np.zeros(s)
    my_mask = np.zeros(s)
    return my_map

def init_rooms():
    """Initializes the rooms in the dungeon."""
    room_number = 0
    total_rooms = random.randrange(min_rooms,max_rooms)
    for i in range(max_iters):
        for r in range(total_rooms):
            x = random.randrange(1,(map_width-min_room_size-1))
            y = random.randrange(1,(map_height-min_room_size-1))
            #Try and keep rooms within the boundaries
            max_width = max_room_size
            max_height = max_room_size
            if max_width >= map_width - x:
                max_width = map_width - x - 1
            if max_height >= map_height - y:
                max_height = map_height - y - 1
            #Don't let rooms get smaller than min size
            if max_width <= min_room_size:
                max_width = min_room_size + 1
            if max_height <= min_room_size:
                max_height = min_room_size + 1
            width = random.randrange(min_room_size,max_width)
            height = random.randrange(min_room_size,max_height)
            room = Room(x,y,width,height)
            if check_room_overlap(room, rooms):
                pass
            else:
                room_number = room_number + 1
                room.room_number = room_number
                rooms.append(room)
            if len(rooms) >= max_rooms:
                break
    for room in rooms:
        for index, row in np.ndenumerate(my_map):
            if index[0] < room.y or index[0] > room.y+room.height or index [1] < room.x or index[1] > room.x+room.width:
                continue
            else:
                my_map[index[0]][index[1]] = 1

def connect_rooms():
    """Draws passages randomly between the rooms."""
    global my_map
    global node_label
    for room in rooms:
        for roomB in rooms:
            #Check if we have a room below our bottom edge
            if roomB.y > room.y + room.height:
                if roomB.x < room.x + room.width and roomB.x + roomB.width > room.x:
                    #print("SOUTH: Connecting Room ["+str(room.room_number)+"] to Room ["+str(roomB.room_number)+"]")
                    lowest_x = max(roomB.x,room.x)
                    highest_x = min(roomB.x+roomB.width,room.x+room.width)
                    starting_point = [random.randint(lowest_x,highest_x), room.y+room.height+1]
                    my_map[starting_point[1]-1][starting_point[0]] = 3
                    newNode = Node(starting_point[0],starting_point[1]-1,node_label)
                    newNode.room = room.room_number
                    room.add_node(newNode)
                    nodes.append(newNode)
                    node_label = chr(ord(node_label) + 1)
                    for y in range(starting_point[1],roomB.y):
                        my_map[y][starting_point[0]] = 2
                    my_map[roomB.y][starting_point[0]] = 3
                    newNode = Node(starting_point[0],roomB.y,node_label)
                    newNode.room = roomB.room_number
                    nodes.append(newNode)
                    roomB.add_node(newNode)
                    node_label = chr(ord(node_label) + 1)
                    break
            #Check if we have a room to the right of our left edge
            if roomB.x > room.x + room.width:
                if roomB.y < room.y + room.height and roomB.y + roomB.height > room.y:
                    #print("EAST: Connecting Room ["+str(room.room_number)+"] to Room ["+str(roomB.room_number)+"]")
                    lowest_y = max(roomB.y,room.y)
                    highest_y = min(roomB.y+roomB.height,room.y+room.height)
                    starting_point = [room.x+room.width+1,random.randint(lowest_y,highest_y)]
                    my_map[starting_point[1]][starting_point[0]-1] = 3
                    newNode = Node(starting_point[0]-1,starting_point[1],node_label)
                    newNode.room = room.room_number
                    nodes.append(newNode)
                    room.add_node(newNode)
                    node_label = chr(ord(node_label) + 1)
                    for x in range(starting_point[0],roomB.x):
                        my_map[starting_point[1]][x] = 2
                    my_map[starting_point[1]][roomB.x] = 3
                    newNode = Node(roomB.x,starting_point[1],node_label)
                    newNode.room = room.room_number
                    nodes.append(newNode)
                    roomB.add_node(newNode)
                    node_label = chr(ord(node_label) + 1)
                    break

def create_entrance():
    #Choose quadrant of map
    #quadrant = random.randint(1,4)
    global node_label
    quadrant = 1
    if quadrant == 1:
        #Start from the left
        rooms_sorted = sort_rooms_x(rooms)
        room_closest = rooms_sorted[0]
        if room_closest.x <= (map_width/15):
            quadrant = quadrant + 1
        else:
            #print("Start from the left, to room: "+str(room_closest.room_number))
            starting_point = [0,random.randint(room_closest.y,room_closest.y+room_closest.height)]
            for x in range(1,room_closest.x):
                my_map[starting_point[1]][x] = 3
            prime_node = Node(room_closest.x,starting_point[1],node_label)
    if quadrant == 2:
        #Start from the bottom
        rooms_sorted = sort_rooms_y(rooms)
        room_closest = rooms_sorted[-1]
        #print("room closest y ["+str(room_closest.y)+"] map height ["+str(map_height)+"]")
        if room_closest.y+room_closest.height >= map_height - (map_height/15):
            quadrant = quadrant + 1
        else:
            #print("Start from the bottom, to room: "+str(room_closest.room_number))
            starting_point = [random.randint(room_closest.x,room_closest.x+room_closest.width),map_height-1]
            #print(starting_point)
            for y in range(room_closest.y+room_closest.height,map_height-1):
                my_map[y][starting_point[0]] = 3
            prime_node = Node(starting_point[0],room_closest.y+room_closest.height,node_label)
    if quadrant == 3:
        #Start from the right
        rooms_sorted = sort_rooms_x(rooms)
        room_closest = rooms_sorted[-1]
        if room_closest.x+room_closest.width >= map_width - (map_width/15):
            quadrant = quadrant + 1
        else:
            #print("Start from the right, to room: "+str(room_closest.room_number))
            starting_point = [map_width-1,random.randint(room_closest.y,room_closest.y+room_closest.height)]
            #print(starting_point)
            for x in range(room_closest.x+room_closest.width,map_width-1):
                my_map[starting_point[1]][x] = 3
            prime_node = Node(room_closest.x+room_closest.width,starting_point[1],node_label)
    if quadrant == 4:
        #Start from the top
        rooms_sorted = sort_rooms_y(rooms)
        room_closest = rooms_sorted[0]
        #print("Start from the top, to room: "+str(room_closest.room_number))
        starting_point = [random.randint(room_closest.x,room_closest.x+room_closest.width),0]
        for y in range(1,room_closest.y):
            my_map[y][starting_point[0]] = 3
        prime_node = Node(starting_point[0],room_closest.y,node_label)
    global pc_point
    pc_point = starting_point
    start_node = Node(pc_point[0],pc_point[1],"start")
    start_node.add_connection(prime_node)
    prime_node.add_connection(start_node)
    prime_node.room = room_closest.room_number
    nodes.append(start_node)
    nodes.append(prime_node)
    node_label = chr(ord(node_label) + 1)

def test_generate():
    init_map()
    init_rooms()
    connect_rooms()
    create_entrance()
    finalMap = Map(map_width,map_height)
    finalMap.matrix = my_map
    finalMap.player_location = pc_point
    finalMap.mask_matrix = my_mask
    for room in rooms:
        finalMap.rooms.append(room)
    for node in nodes:
        finalMap.nodes.append(node)
    draw_dungeon(finalMap, fogOfWar=True)

if __name__ == "__main__":
    test_generate()

def __str__(self):
    return f"A room at ({self.x},{self.y})"