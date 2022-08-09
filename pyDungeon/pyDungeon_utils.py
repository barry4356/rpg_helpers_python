#pyDungeon_utils.py
import cairo

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
        
def draw_dungeon(my_map, map_width, map_height, rooms, nodes, pc_point, map_name="Map Name"):
    """Draw the dungeon with cario rectangles."""
    """If the Room coordinates are provided, add labels."""
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24,map_width*10,map_height*10)
    ctx = cairo.Context(surface)
    for y in range(map_height):
        for x in range(map_width):
            if x == pc_point[0] and y == pc_point[1]:
                ctx.set_source_rgb(1,1,1)
            elif my_map[y][x] == 0:
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
