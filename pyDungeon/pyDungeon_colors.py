#pyDungeon_colors.py

import enum

darkGray    = [0.3,0.3,0.3]
lightGray   = [0.5,0.5,0.5]
Red         = [1,0,0]
DarkRed     = [0.5,0,0]

class map_matrix_enum(enum.Enum):
    wall = 0
    room = 1
    hall = 2
    node = 3