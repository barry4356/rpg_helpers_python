import cairo
import random
import numpy as np
from pyDungeon_utils import check_room_overlap
from pyDungeon_utils import sort_rooms_x
from pyDungeon_hallways import connect_points

map_width = 50 # number of squares wide
map_height = 50 # number of squares tall

min_room_size = 4
max_room_size = 20
max_rooms = 10
min_rooms = 5
max_iters = 3
rooms = []
my_map = []

def init_map():
    """Initializes the map of key/value pairs."""
    global my_map
    s = (map_height,map_width)
    my_map = np.zeros(s)
    return my_map

class Room:
    """Defines a room of the dungeon."""
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.room_number = 0

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
    for room in rooms:
        #print("Room: ["+str(room.room_number)+"] Width: ["+str(room.width)+"] Height: ["+str(room.height)+"]")
        first_point = []
        second_point = []
        #Right->Left, Right->Bottom, Right->Top
        rl = False
        rb = False
        rt = False
        first_elbow = random.randint(int(room.width*.3),int(room.width*.5))
        #Either add hallway to the right edge
        if random.randint(0, 1) == 1:
            for roomB in rooms:
                if roomB.x > room.x + room.width + first_elbow:
                    first_point = [room.x+room.width,random.randint(room.y,room.y+room.height)]
                    if roomB.y < first_point[1] - first_elbow - roomB.height and roomB.x > room.x+room.width:
                        second_point = [random.randint(roomB.x,roomB.x+room.width),roomB.y+roomB.height]
                        print("RB- Room ["+str(room.room_number)+"] Connect to Room ["+str(roomB.room_number)+"]")
                        rb = True
        else:
        #Or the bottom edge
            print()
        if first_point and second_point:
            if rb == True:
                current_point=first_point
                for i in range(first_elbow):
                    my_map[current_point[1]][current_point[0]] = 1
                    current_point = [current_point[0]+1,current_point[1]]
                for i in range(second_point[1],current_point[1]):
                    my_map[current_point[1]][current_point[0]] = 1
                    current_point = [current_point[0],current_point[1]-1]

    #random.shuffle(rooms)
    #sorted_rooms_x = sort_rooms_x(rooms)
    #roomA = rooms[0]
    #roomB = rooms[0]
    #for i in range(len(rooms)-1):
    #    roomA = rooms[i]
    #    roomB = rooms[i+1]
    #for x in range(roomA.x,roomB.x):
    #    my_map[x][roomA.y] = 1
    #for y in range(roomA.y, roomB.y):
    #    my_map[roomA.x][y] = 1
    #for x in range(roomB.x,roomA.x):
    #    my_map[x][roomA.y] = 1
    #for y in range(roomB.y, roomA.y):
    #    my_map[roomA.x][y] = 1

def draw_dungeon(map_name="Map Name"):
    """Draw the dungeon with cario rectangles."""
    """If the Room coordinates are provided, add labels."""
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24,map_width*10,map_height*10)
    ctx = cairo.Context(surface)
    for y in range(map_height):
        for x in range(map_width):
            if my_map[y][x] == 0:
                ctx.set_source_rgb(0.3,0.3,0.3)
            else:
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
    #Write to png file
    surface.write_to_png("dungeon.png")
    print("Total rooms: " + str(len(rooms)))

def generate_dungeon():
    init_map()
    init_rooms()
    #connect_rooms()
    draw_dungeon()

if __name__ == "__main__":
    generate_dungeon()

def __str__(self):
    return f"A room at ({self.x},{self.y})"