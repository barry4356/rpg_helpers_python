#pyDungeon_utils.py
import cairo
import numpy as np
import pyDungeon_colors

#Check if a room overlaps with any in the list
def check_room_overlap(room, rooms):
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

#Sort rooms by room.x value
def sort_rooms_x(rooms):
    rooms_sorted = rooms
    rooms_sorted.sort(key=lambda x: x.x)
    return rooms_sorted

#Sort rooms by room.x value
def sort_rooms_y(rooms):
    rooms_sorted = rooms
    rooms_sorted.sort(key=lambda x: x.y)
    return rooms_sorted
        
def draw_dungeon(my_map, fogOfWar=False, filename=""):
    """Draw the dungeon with cario rectangles."""
    """If fog of war is enabled, include the mask."""
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24,my_map.map_width*10,my_map.map_height*10)
    ctx = cairo.Context(surface)
    for y in range(my_map.map_height):
        for x in range(my_map.map_width):
            if x == my_map.player_location[0] and y == my_map.player_location[1]:
                ctx.set_source_rgb(*pyDungeon_colors.White)
            elif fogOfWar and my_map.mask_matrix[y][x] == 0:
                ctx.set_source_rgb(*pyDungeon_colors.darkGray)
            elif my_map.matrix[y][x] == pyDungeon_colors.wall_enum:
                ctx.set_source_rgb(*pyDungeon_colors.darkGray)
            elif my_map.matrix[y][x] == pyDungeon_colors.room_enum:
                ctx.set_source_rgb(*pyDungeon_colors.lightGray)
            elif my_map.matrix[y][x] == pyDungeon_colors.hall_enum:
                ctx.set_source_rgb(*pyDungeon_colors.lightGray)
            elif my_map.matrix[y][x] == pyDungeon_colors.node_enum:
                ctx.set_source_rgb(*pyDungeon_colors.lightGray)
            ctx.rectangle(x*10, y*10, 10, 10)
            ctx.fill()
    # Draw Map Label
    ctx.set_source_rgb(*pyDungeon_colors.Red)
    ctx.set_font_size(my_map.map_width / 3)
    ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
    ctx.move_to(my_map.map_width/4, my_map.map_width/1.5)
    ctx.show_text(my_map.map_name)
    #Draw Room Labels
    for room in my_map.rooms:
        ctx.set_source_rgb(*pyDungeon_colors.Red)
        ctx.set_font_size(my_map.map_width / 3)
        ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
        label_x = int(room.x+.5*room.width)
        label_y = int(room.y+.5*room.height)
        if not (fogOfWar and my_map.mask_matrix[label_y][label_x] == 0):
            ctx.move_to(label_x*10, label_y*10)
            ctx.show_text(str(room.room_number))
    #Draw Node Labels
    for node in my_map.nodes:
        ctx.set_source_rgb(*pyDungeon_colors.DarkRed)
        ctx.set_font_size(my_map.map_width / 4)
        ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
        if not (fogOfWar and my_map.mask_matrix[node.y][node.x] == 0):
            ctx.move_to((node.x)*10, (node.y)*10)
            ctx.show_text(str(node.label))
    #Write to png file
    if filename:
        surface.write_to_png(filename)
    else:
        surface.write_to_png(my_map.map_name+".png")
    #print("Total rooms: " + str(len(my_map.rooms)))

#update our mask to reveal a room
def unmask_room(mask_matrix,room):
    for index, row in np.ndenumerate(mask_matrix):
            if index[0] < room.y or index[0] > room.y+room.height or index [1] < room.x or index[1] > room.x+room.width:
                continue
            else:
                mask_matrix[index[0]][index[1]] = 1
    return mask_matrix

#update our mask to reveal map between two points
def unmask_line(mask_matrix,point1,point2):
    #If we have a line down the x axis
    if point1[0] == point2[0]:
        x = point1[0]
        for y in range(point1[1],point2[1]):
            mask_matrix[y][x] = 1
        for y in range(point2[1],point1[1]):
            mask_matrix[y][x] = 1
    #If we have a line down the y axis
    elif point1[1] == point2[1]:
        y = point1[1]
        for x in range(point1[0],point2[0]):
            mask_matrix[y][x] = 1
        for x in range(point2[0],point1[0]):
            mask_matrix[y][x] = 1
    else:
    #If we have some other line
        for x in range(point1[0],point2[0]):
            for y in range(point1[1],point2[1]):
                mask_matrix[y][x] = 1
            for y in range(point2[1],point1[1]):
                mask_matrix[y][x] = 1
    return mask_matrix

def unmask_nodes(mask_matrix,node1,node2):
    mask_matrix=unmask_node(mask_matrix,node1)
    mask_matrix=unmask_node(mask_matrix,node2)
    mask_matrix=unmask_line(mask_matrix,[node1.x,node1.y],[node2.x,node2.y])
    return mask_matrix

def unmask_node(mask_matrix,node):
    mask_matrix[node.y][node.x]=1
    return mask_matrix

def find_node(nodes,label):
    for node in nodes:
        if node.label == label:
            return node

def find_room(rooms,room_number):
    for room in rooms:
        if room.room_number == room_number:
            return room