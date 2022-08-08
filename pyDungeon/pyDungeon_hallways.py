#pyDungeon_hallways.py

def print_nodes(nodes=[]):
    if not nodes:
        return
    for node in nodes:
        print()
        print("Node ["+node.label+"]")
        print("Location ["+str(node.x)+","+str(node.y)+"]")
        print("Connections:")
        for connection in node.connections:
            print("\t["+connection+"]")
        print("Room: ["+str(node.room)+"]")
        print("==========")