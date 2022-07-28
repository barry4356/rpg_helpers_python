#hexmap_utils.py
import utils
import hexmath

def get_hex_context(tile):
    layer = hexmath.get_layer(tile)
    north_edge, ne_edge, east_edge, se_edge, south_edge, sw_edge, west_edge, nw_edge = hexmath.get_hex_edges(layer)
    print("Tile ["+str(tile)+"] is located in ring number ["+str(layer)+"]")
    print("Points for Bearings:")
    print("\t\tNorth ["+str(north_edge)+"]")
    print("\tNW ["+str(nw_edge)+"]\t\t["+str(ne_edge)+"] NE")
    if west_edge or east_edge:
        print("WEST ["+str(west_edge)+"]\t\t\t["+str(east_edge)+"] East")
    print("\tSW ["+str(sw_edge)+"]\t\t["+str(se_edge)+"] SE")
    print("\t\tSOUTH ["+str(south_edge)+"]")

def hexcontext_menu():
    print("What tile are you looking for context for?")
    val = utils.get_input_int()
    get_hex_context(val)

def menu():
    func_list = [hexcontext_menu]
    desc_list = ["Get Context for Hex Tile"]
    utils.menu(func_list,desc_list,"Hexmap Utils",False)