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
    def add_node(node):
        self.nodes.append(node.label)

class Node:
    """Defines a coordinate point that can be navigated through."""
    def __init__(self,x,y,label):
        self.x = x
        self.y = y
        self.label = label
        self.connections = []
    def add_connection(node):
        self.connections.append([node.label])