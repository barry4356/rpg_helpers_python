#hexmap_utils.py
import utils
import hexmath
import dice

def compare_hex_tiles(tile1, tile2):
    distance = hexmath.tile_distance(tile1, tile2)
    bearing = hexmath.tile_bearing(tile1, tile2)
    print("Origin: Tile ["+str(tile1)+"] \nDestination: Tile ["+str(tile2)+"]")
    print("Distance: ["+str(int(distance))+"] Tiles")
    print("Bearing: ["+str(bearing)+"]")

def get_hex_context(tile):
    layer = hexmath.get_layer(tile)
    north_edge, ne_edge, east_edge, se_edge, south_edge, sw_edge, west_edge, nw_edge = hexmath.get_hex_edges(layer)
    print("Tile ["+str(tile)+"] is located in ring number ["+str(layer)+"]")
    print("Points for Bearings:")
    print("\t\tNORTH ["+str(north_edge)+"]")
    print("\tNW ["+str(nw_edge)+"]          ["+str(ne_edge)+"] NE")
    if west_edge or east_edge:
        print("WEST ["+str(west_edge)+"]\t\t\t["+str(east_edge)+"] EAST")
    print("\tSW ["+str(sw_edge)+"]          ["+str(se_edge)+"] SE")
    print("\t\tSOUTH ["+str(south_edge)+"]")

def hexcontext_menu():
    print("What tile are you looking for context for?")
    val = utils.get_input_int()
    get_hex_context(val)

def random_hex_in_area(center_tile=0, min_radius=0, max_radius=0):
    for index in range (10000):
        random_tile = dice.roll_custom(1000)
        distance = hexmath.tile_distance(center_tile,random_tile)
        if distance <= max_radius and distance >= min_radius:
            return random_tile
    return 0

def menu():
    func_list = [hexcontext_menu]
    desc_list = ["Get Context for Hex Tile"]
    utils.menu(func_list,desc_list,"Hexmap Utils",False)