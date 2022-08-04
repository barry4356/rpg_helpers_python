import cairo
import random

map_width = 50 # number of squares wide
map_height = 50 # number of squares tall
my_map = []

min_room_size = 6
max_room_size = 20
max_rooms = 10
min_rooms = 3
max_iters = 3
rooms = []

def check_for_overlap(room, rooms):
    """Return false if the room overlaps any other room."""
    for current_room in rooms:
        xmin1 = room.x
        xmax1 = room.x + room.width
        xmin2 = current_room.x
        xmax2 = current_room.x + current_room.width
        ymin1 = room.y
        ymax1 = room.y + room.height
        ymin2 = current_room.y
        ymax2 = current_room.y + current_room.height
        if (xmin1 <= xmax2 and xmax1 >= xmin2) and \
           (ymin1 <= ymax2 and ymax1 >= ymin2):
            return True
    return False


def init_map():
    """Initializes the map of key/value pairs."""
    my_width = [0] * map_width
    for index in range(map_height):
        my_map.append(my_width)

class Room:
    """Defines a room of the dungeon."""
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def init_rooms():
    """Initializes the rooms in the dungeon."""
    total_rooms = random.randrange(min_rooms,max_rooms)
    for i in range(max_iters):
        for r in range(total_rooms):
            if len(rooms) >= max_rooms:
                break
    x = random.randrange(0,map_width)
    y = random.randrange(0,map_height)
    width = random.randrange(min_room_size,max_room_size)
    height = random.randrange(min_room_size,max_room_size)
    room = Room(x,y,width,height)
    if check_for_overlap(room, rooms):
        pass
    else:
        rooms.append(room)
    for room in rooms:
        for y in range(room.y, room.y+room.height):
            for x in range(room.x, room.x+room.width):
                if x < map_width and y < map_height:
                    my_map[x][y] = 1

def connect_rooms():
    """Draws passages randomly between the rooms."""
    random.shuffle(rooms)
    roomA = rooms[0]
    roomB = rooms[0]
    for i in range(len(rooms)-1):
        roomA = rooms[i]
        roomB = rooms[i+1]
    for x in range(roomA.x,roomB.x):
        my_map[x][roomA.y] = 1
    for y in range(roomA.y, roomB.y):
        my_map[roomA.x][y] = 1
    for x in range(roomB.x,roomA.x):
        my_map[x][roomA.y] = 1
    for y in range(roomB.y, roomA.y):
        my_map[roomA.x][y] = 1

def draw_dungeon():
    for index in range(len(my_map)):
        print(my_map[index])
    """Draw the dungeon with cario rectangles."""
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24,500,500)
    ctx = cairo.Context(surface)
    for y in range(50):
        for x in range(50):
            r = random.randrange(1,10)
            if my_map[x][y] == 0:
                ctx.set_source_rgb(0.3,0.3,0.3)
            else:
                ctx.set_source_rgb(0.5,0.5,0.5)
            ctx.rectangle(x*10, y*10, 10, 10)
            ctx.fill()
    surface.write_to_png("dungeon.png")
    print("Total rooms: " + str(len(rooms)))

def generate_dungeon():
    init_map()
    init_rooms()
    connect_rooms()
    draw_dungeon()

if __name__ == "__main__":
    generate_dungeon()

def __str__(self):
    return f"A room at ({self.x},{self.y})"





