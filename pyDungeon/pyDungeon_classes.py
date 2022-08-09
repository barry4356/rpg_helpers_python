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
    def print_room():
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
    def print_node():
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
    def __init__(self,x,y,label):
        self.rooms = []
        self.nodes = []
        self.matrix = []
        self.player_location = []
        self.room = ""