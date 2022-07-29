#hex_test.py
import hexmath
import fileops

def test_dict_utils():
    fileops.serialize_dict({"key1":"value1","key2":"value2"},"results.txt")
    my_dict = fileops.deserialize_dict("results.txt")
    print(my_dict)

def test_get_layer():
    for tilenum in range(61):
        layer = hexmath.get_layer(tilenum)
        print("Tile: "+str(tilenum)+" Layer: "+str(layer))

def test_hex_to_coord():
    for tilenum in range(128):
        north, west = hexmath.hex_to_coord(tilenum)
        #print("Tile ["+str(tilenum)+"] N/W ["+str(north)+","+str(west)+"]")
        if north == 0 and west == 0:
            print("Tile ["+str(tilenum)+"] N/W ["+str(north)+","+str(west)+"]")

def test_coord_to_hex():
    for north in range(7):
        for west in range(7):
            tilenum = hexmath.coord_to_hex(north,west)
            print("Coordinates: ["+str(north)+","+str(west)+"] tile: "+str(tilenum))

def test_layer_min_max():
    for layer in [1,2,3,4]:
        layer_min, layer_max = hexmath.layer_min_max(layer)
        print("Layer ["+str(layer)+"] Min ["+str(layer_min)+"] Max ["+str(layer_max)+"]")

def test_tile_distance():
    for tile in [1,2,3,4,60]:
        for tile2 in [10,11,12,13,45]:
            distance = int(hexmath.tile_distance(tile,tile2))
            print("Tile1 ["+str(tile)+"] Tile 2["+str(tile2)+"] Distance ["+str(distance)+"]")

def test_get_hex_edges():
    for layer in [5,2]:
        print("Layer: "+str(layer)+" edges: ")
        print(hexmath.get_hex_edges(layer))

print("Testing get_layer...")
test_get_layer()
print()
print("Testing layer_min_max...")
test_layer_min_max()
print()
print("Testing hex_to_coord...")
test_hex_to_coord()
print()
print("Testing coord_to_hex...")
test_coord_to_hex()
print()
print("Testing tile_distance...")
test_tile_distance()
print()
print("Testing get_hex_edges...")
test_get_hex_edges()
print()
print("Testing some dict utils...")
test_dict_utils()
print()