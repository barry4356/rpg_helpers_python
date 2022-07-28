#hexmath.py
import utils

def get_hex_edges(layer_num):
    layer_min, layer_max = layer_min_max(layer_num)
    layer_size = layer_max - layer_min + 1
    north_edge = layer_min
    ne_edge = layer_min + (layer_num-1)
    se_edge = layer_min + (2 * (layer_num-1))
    south_edge = layer_min + (3 * (layer_num - 1))
    sw_edge = layer_min + (4 * (layer_num - 1))
    nw_edge = layer_min + (5 * (layer_num - 1))
    east_edge = 0
    west_edge = 0
    if layer_num % 2 != 0:
    #If layer is odd, consider east/west edges
        if ((north_edge + south_edge) / 2).is_integer():
            east_edge = int(((north_edge + south_edge) / 2))
            west_edge = south_edge + (south_edge - east_edge)
    return north_edge, ne_edge, east_edge, se_edge, south_edge, sw_edge, west_edge, nw_edge

def tile_distance(tile1, tile2):
    coord1 = hex_to_coord(tile1)
    coord2 = hex_to_coord(tile2)
    return coord_distance(coord1,coord2)

def tile_bearing(tile1, tile2):
    coord1 = hex_to_coord(tile1)
    coord2 = hex_to_coord(tile2)
    return coord_bearing(coord1,coord2)

def coord_bearing(coord1=[],coord2=[]):
    if len(coord1) != 2 or len(coord2) != 2:
        return ""
    if coord1[0] < coord2[0]:
        if coord1[1] == coord2[1]:
            return "N"
        elif coord1[1] < coord2[1]:
            return "NE"
        elif coord1[1] > coord2[1]:
            return "NW"
    elif coord1[0] == coord2[0]:
        if coord1[1] < coord2[1]:
            return "E"
        elif coord1[1] > coord2[1]:
            return "W"
    elif coord1[0] > coord2[0]:
        if coord1[1] == coord2[1]:
            return "S"
        elif coord1[1] < coord2[1]:
            return "SE"
        elif coord1[1] > coord2[1]:
            return "SW"
    return ""

def coord_distance(coord1=[],coord2=[]):
    if len(coord1) != 2 or len(coord2) != 2:
        return 0
    return utils.sqrt(((abs(coord1[0] - coord2[0])) * (abs(coord1[0] - coord2[0]))) + ((abs(coord1[1] - coord2[1])) * (abs(coord1[1] - coord2[1]))))

def coord_split_dif(coord1=[],coord2=[]):
    if len(coord1) != 2 or len(coord2) != 2:
        return 0
    return [int((coord1[0]+coord2[0])/2),int((coord1[1]+coord2[1])/2)]

# Get a tile number, and determine which layer we're in
# (Tile 1 is center, each 'layer' is another ring around center)
def get_layer(hextile):
    layer_size = 0
    layer = 1
    layer_max = 1
    end = False
    while end != True:
        if hextile > layer_max:
            layer_size = layer_size + 6
            layer = layer + 1
            layer_max = layer_max + layer_size
        else:
            return layer

# Find min/max of a given layer
def layer_min_max(layer):
    layer_min = 0
    layer_max = 1
    layer_size = 0
    for i in range(layer-1):
        layer_size = layer_size + 6
        layer_min = layer_max + 1
        layer_max = layer_min + layer_size - 1
    return(layer_min,layer_max)

#Convert N/W Coordinates to hex tile
def coord_to_hex(north,west):
    input_coords=[north,west]
    layer_num = max([abs(north)+1,abs(west)+1])
    layer_min, layer_max = layer_min_max(layer_num)
    #Derive our coordinate edge-points
    north_edge = [layer_num-1,0]
    ne_edge = [layer_num-1,layer_num-1]
    east_edge = [0,layer_num-1]
    se_edge = [(layer_num-1)*-1,layer_num-1]
    south_edge = [(layer_num-1)*-1,0]
    sw_edge = [(layer_num-1)*-1,(layer_num-1)*-1]
    west_edge = [0,(layer_num-1)*-1]
    nw_edge = [layer_num-1,(layer_num-1)*-1]
    #Derive our hex equivalents
    north_tile = layer_min
    ne_tile = layer_min + (layer_num-1)
    se_tile = layer_min + (2 * (layer_num-1))
    east_tile = int(((se_tile - ne_tile) / 2) + ne_tile)
    south_tile = layer_min + (3 * (layer_num - 1))
    sw_tile = layer_min + (4 * (layer_num - 1))
    nw_tile = layer_min + (5 * (layer_num - 1))
    west_tile = int(((nw_tile - sw_tile) / 2) + sw_tile)
    #Check if we are sitting on an end-point
    if input_coords == north_edge:
        return north_tile
    elif input_coords == ne_edge:
        return ne_tile
    elif input_coords == se_edge:
        return se_tile
    elif input_coords == east_edge:
        return east_tile
    elif input_coords == south_edge:
        return south_tile
    elif input_coords == sw_edge:
        return sw_tile
    elif input_coords == nw_edge:
        return nw_tile
    elif input_coords == west_edge:
        return west_tile
    #Find the closest edge coordinates to us
    closest_edges = []
    for near_edge1 in [north_edge,ne_edge,se_edge,east_edge,south_edge,sw_edge,nw_edge,west_edge]:
        strikes = []
        distance1 = coord_distance(input_coords,near_edge1)
        for near_edge2 in [north_edge,ne_edge,se_edge,east_edge,south_edge,sw_edge,nw_edge,west_edge]:
            distance2 = coord_distance(input_coords,near_edge2)
            if distance2 < distance1:
                strikes.append("strike")
            if len(strikes) > 1:
                break
        if len(strikes) < 2:
            closest_edges.append(near_edge1)
        if len(closest_edges) == 2:
            break
    #print(closest_edges)
    #Use our two nearest edge coordinates to find our nearest tiles
    closest_tiles = []
    if closest_edges[0] == north_edge or closest_edges[1] == north_edge:
        closest_tiles.append(north_tile)
    if closest_edges[0] == ne_edge or closest_edges[1] == ne_edge:
        closest_tiles.append(ne_tile)
    if closest_edges[0] == east_edge or closest_edges[1] == east_edge:
        closest_tiles.append(east_tile)
    if closest_edges[0] == se_edge or closest_edges[1] == se_edge:
        closest_tiles.append(se_tile)
    if closest_edges[0] == south_edge or closest_edges[1] == south_edge:
        closest_tiles.append(south_tile)
    if closest_edges[0] == sw_edge or closest_edges[1] == sw_edge:
        closest_tiles.append(sw_tile)
    if closest_edges[0] == west_edge or closest_edges[1] == west_edge:
        closest_tiles.append(west_tile)
    if closest_edges[0] == nw_edge or closest_edges[1] == nw_edge:
        closest_tiles.append(nw_tile)
    #Split the difference between closest tiles
    if len(closest_tiles) >= 2:
        return int((closest_tiles[0] + closest_tiles[1]) / 2)
    return 0
    

#Convert a hex tile to a N/W Coordinate
def hex_to_coord(tile):
    layer_num = get_layer(tile)
    layer_min, layer_max = layer_min_max(layer_num)
    layer_size = layer_max - layer_min + 1
    ##
    ### CHECK FOR EASY CONVERSIONS FIRST###
    north_edge = layer_min
    ne_edge = layer_min + (layer_num-1)
    se_edge = layer_min + (2 * (layer_num-1))
    south_edge = layer_min + (3 * (layer_num - 1))
    sw_edge = layer_min + (4 * (layer_num - 1))
    nw_edge = layer_min + (5 * (layer_num - 1))
    east_edge = 0
    west_edge = 0
    if layer_num % 2 != 0:
    #If layer is odd, consider east/west edges
        if ((north_edge + south_edge) / 2).is_integer():
            east_edge = int(((north_edge + south_edge) / 2))
            west_edge = south_edge + (south_edge - east_edge)
            #print("East Edge: "+str(east_edge))
            #print("West Edge: "+str(west_edge))

    # Check for due-north case
    if tile == north_edge:
        return (layer_num-1,0)
    # Check for direct north-east
    if tile == ne_edge:
        return(layer_num-1,layer_num-1)
    # Check for due East
    if tile == east_edge:
        return(0,layer_num-1)
    # Check for direct south-east
    if tile == se_edge:
        return((layer_num*-1)+1,layer_num-1)
    # Check for due-south case
    if tile == south_edge:
        return ((layer_num * -1)+1, 0)
    # Check for direct south-west
    if tile == sw_edge:
        return((layer_num*-1)+1,(layer_num*-1)+1)
    # Check for due west
    if tile == west_edge:
        return(0,(layer_num*-1)+1)
    # Check for direct north-west
    if tile == nw_edge:
        return(layer_num-1,(layer_num*-1)+1)
    ###
    # If we get here... we're not on a direct track
    # and the math gets.... weird
    # Step 1: Divide the layer into sixths
    # Step 2: Find our nearest edge (direct track)
    # Step 3: find coordinates of nearest edge
    # Step 4: ~Somehow derive our coordinates from those~
    closest_edge = "North"
    closest_distance = abs(tile-north_edge)
    closest_tile = north_edge
    if (abs(tile - ne_edge)) < closest_distance:
        closest_distance = abs(tile-ne_edge)
        closest_tile = ne_edge
        closest_edge = "NorthEast"
    if (abs(tile - se_edge)) < closest_distance:
        closest_distance = abs(tile-se_edge)
        closest_tile = se_edge
        closest_edge = "SouthEast"
    if (abs(tile - south_edge)) < closest_distance:
        closest_distance = abs(tile-south_edge)
        closest_tile = south_edge
        closest_edge = "South"
    if (abs(tile - sw_edge)) < closest_distance:
        closest_distance = abs(tile-sw_edge)
        closest_tile = sw_edge
        closest_edge = "SouthWest"
    if (abs(tile - nw_edge)) < closest_distance:
        closest_distance = abs(tile-nw_edge)
        closest_tile = nw_edge
        closest_edge = "NorthWest"
    if (abs(tile - layer_max) < closest_distance):
        closest_edge = "North"
        closest_tile = north_edge
        closest_distance = abs(tile-layer_max)
    if (abs(tile - east_edge) < closest_distance):
        closest_edge = "East"
        closest_tile = east_edge
        closest_distance = abs(tile-east_edge)
    if (abs(tile - west_edge) < closest_distance):
        closest_edge = "West"
        closest_tile = west_edge
        closest_distance = abs(tile-west_edge)
    nearest_coords=[0,0]
    nearest_coords[0],nearest_coords[1] = hex_to_coord(closest_tile)
    #Deriving our new coordinates
    if closest_edge == "North":
        if tile > south_edge:
            #We are S/W of Northern point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] - utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] - utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        else:
            #We are S/E of Northern point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] - utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] + utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
    elif tile - closest_tile <= 0:
        #We are going clockwise
        if closest_edge == "NorthEast":
            #We are N/W of point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] - utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] - utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        elif closest_edge == "East":
            #We are W of point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] + utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] - utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        elif closest_edge == "SouthEast":
            #We are W of point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] + utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] - utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        elif closest_edge == "South":
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] - utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] + utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        elif closest_edge == "SouthWest":
            #We are W of point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] + utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] + utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        elif closest_edge == "West":
            #We are W of point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] - utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] + utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        elif closest_edge == "NorthWest":
            #We are W of point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] - utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] + utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
    else:
        #We are going counter-clockwise
        if closest_edge == "NorthEast":
            #We are N/W of point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] - utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] - utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        elif closest_edge == "East":
            #We are W of point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] - utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] - utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        elif closest_edge == "SouthEast":
            #We are W of point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] + utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] - utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        elif closest_edge == "South":
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] + utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] - utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        elif closest_edge == "SouthWest":
            #We are W of point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] + utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] + utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        elif closest_edge == "West":
            #We are W of point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] + utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] + utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
        elif closest_edge == "NorthWest":
            #We are W of point
            my_coords = nearest_coords
            my_coords[0] = my_coords[0] - utils.round(closest_distance/2)
            my_coords[1] = my_coords[1] + utils.round(closest_distance/2)
            return my_coords[0],my_coords[1]
    return 0,0
