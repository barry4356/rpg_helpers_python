#pyDungeon_utils.py

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