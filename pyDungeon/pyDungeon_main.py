import cairo
import random
import numpy as np
from pyDungeon_utils import check_room_overlap
from pyDungeon_utils import sort_rooms_x
from pyDungeon_utils import print_rooms
from pyDungeon_hallways import print_nodes
from pyDungeon_classes import Room
from pyDungeon_classes import Node

map_width = 55 # number of squares wide
map_height = 55 # number of squares tall

min_room_size = 4
max_room_size = 20
max_rooms = 14
min_rooms = 12
max_iters = 3
rooms = []
my_map = []
my_nodex = []
node_label = 'a'
nodes = []

def init_map():
    """Initializes the map of key/value pairs."""
    global my_map
    s = (map_height,map_width)
    my_map = np.zeros(s)
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

def draw_dungeon(map_name="Map Name"):
    """Draw the dungeon with cario rectangles."""
    """If the Room coordinates are provided, add labels."""
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24,map_width*10,map_height*10)
    ctx = cairo.Context(surface)
    for y in range(map_height):
        for x in range(map_width):
            if my_map[y][x] == 0:
                ctx.set_source_rgb(0.3,0.3,0.3)
            elif my_map[y][x] == 1:
                ctx.set_source_rgb(0.5,0.5,0.5)
            elif my_map[y][x] == 2:
                ctx.set_source_rgb(0.4,0.4,0.4)
            elif my_map[y][x] == 3:
                ctx.set_source_rgb(0.5,0.5,0.5)
            ctx.rectangle(x*10, y*10, 10, 10)
            ctx.fill()
    # Draw Map Label
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_font_size(map_width / 3)
    ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
    ctx.move_to(map_width/4, map_width/1.5)
    ctx.show_text(map_name)
    #Draw Room Labels
    for room in rooms:
        ctx.set_source_rgb(1, 0, 0)
        ctx.set_font_size(map_width / 3)
        ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
        ctx.move_to((room.x+.5*room.width)*10, (room.y+.5*room.height)*10)
        ctx.show_text(str(room.room_number))
    #Draw Node Labels
    for node in nodes:
        ctx.set_source_rgb(0.5, 0, 0)
        ctx.set_font_size(map_width / 4)
        ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
        ctx.move_to((node.x)*10, (node.y)*10)
        ctx.show_text(str(node.label))
    #Write to png file
    surface.write_to_png("dungeon.png")
    print("Total rooms: " + str(len(rooms)))

def test_generate():
    init_map()
    init_rooms()
    connect_rooms()
    #print_nodes(nodes)
    print_rooms(rooms)
    draw_dungeon()

if __name__ == "__main__":
    test_generate()

def __str__(self):
    return f"A room at ({self.x},{self.y})"