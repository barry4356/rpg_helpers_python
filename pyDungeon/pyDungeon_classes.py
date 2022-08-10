#pyDungeon_classes.py

class Room:
    """Defines a room of the dungeon."""
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.room_number = 0
        self.nodes = []
    def add_node(self,node):
        self.nodes.append(node.label)
    def print_room(self):
        print("Room: ["+str(self.room_number)+"]")
        for node in self.nodes:
            print("\tNode: ["+node+"]")
        print("")

class Node:
    """Defines a coordinate point that can be navigated through."""
    def __init__(self,x,y,label):
        self.x = x
        self.y = y
        self.label = label
        self.connections = []
        self.room = ""
    def add_connection(self,node):
        self.connections.append([node.label])
    def print_node(self):
        print()
        print("Node ["+self.label+"]")
        print("Location ["+str(self.x)+","+str(self.y)+"]")
        print("Connections:")
        for connection in self.connections:
            print("\t["+str(connection)+"]")
        print("Room: ["+str(self.room)+"]")
        print("==========")

class Map:
    """Defines a full set of map data."""
    def __init__(self, map_width, map_height, map_name="Map Name"):
        self.map_name = map_name
        self.map_width = map_width
        self.map_height = map_height
        self.rooms = []
        self.nodes = []
        self.matrix = []
        self.mask_matrix = []
        self.player_location = []
    def print_map(self):
        print("-------------------")
        print("Map Name: "+self.map_name)
        print("Map Width: "+str(self.map_width))
        print("Map Height: "+str(self.map_height))
        print("Player Location: "+str(self.player_location))
        for room in self.rooms:
            room.print_room()
        for node in self.nodes:
            node.print_node()