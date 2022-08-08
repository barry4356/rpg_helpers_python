import cairo
import random
import numpy as np

map_width = 50 # number of squares wide
map_height = 50 # number of squares tall

min_room_size = 4
max_room_size = 20
max_rooms = 10
min_rooms = 5
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
        if (xmin1 <= xmax2+1 and xmax1 >= xmin2-1) and \
           (ymin1 <= ymax2+1 and ymax1 >= ymin2-1):
            return True
    return False


def init_map():
    """Initializes the map of key/value pairs."""
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

def init_rooms(my_map):
    """Initializes the rooms in the dungeon."""
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
            if check_for_overlap(room, rooms):
                pass
            else:
                rooms.append(room)
            if len(rooms) >= max_rooms:
                break
    for room in rooms:
        for index, row in np.ndenumerate(my_map):
            if index[0] < room.y or index[0] > room.y+room.height or index [1] < room.x or index[1] > room.x+room.width:
                continue
            else:
                my_map[index[0]][index[1]] = 1
    return(my_map)

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

def draw_dungeon(my_map, map_name="Map Name"):
    """Draw the dungeon with cario rectangles."""
    """If the Room coordinates are provided, add labels."""
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24,map_width*10,map_height*10)
    ctx = cairo.Context(surface)
    for y in range(map_height):
        for x in range(map_width):
            if my_map[x][y] == 0:
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
    room_number = 0
    for room in rooms:
        room_number = room_number + 1
        ctx.set_source_rgb(1, 0, 0)
        ctx.set_font_size(map_width / 3)
        ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
        ctx.move_to((room.y+.5*room.height)*10, (room.x+.5*room.width)*10)
        ctx.show_text(str(room_number))
    #Write to png file
    surface.write_to_png("dungeon.png")
    print("Total rooms: " + str(len(rooms)))

def generate_dungeon():
    my_map = init_map()
    my_map = init_rooms(my_map)
    #connect_rooms()
    draw_dungeon(my_map)

if __name__ == "__main__":
    generate_dungeon()

def __str__(self):
    return f"A room at ({self.x},{self.y})"