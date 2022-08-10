#mappa_imperium_helper.py
import utils
import pyDungeon_main
import pyDungeon_utils
from PIL import Image
import psutil

def generate_map():
    return pyDungeon_main.demo_generate()

def main_menu():
    my_map = generate_map()
    my_node = pyDungeon_utils.find_node(my_map.nodes,"start")
    first_node = pyDungeon_utils.find_node(my_map.nodes,my_node.connections[0][0])
    if first_node:
        my_map.mask_matrix = pyDungeon_utils.unmask_nodes(my_map.mask_matrix,my_node,first_node)
        pyDungeon_utils.draw_dungeon(my_map,fogOfWar=True)
        pyDungeon_utils.draw_dungeon(my_map,fogOfWar=False,filename="DemoDungeonRevealed.png")
    utils.print_header("Dungeon Crawler Demo")
    exit_now = False
    while exit_now != True:
        current_room_number = 0
        direction_options = []
        direction_options.append(my_node.connections[0][0])
        my_map.mask_matrix = pyDungeon_utils.unmask_node(my_map.mask_matrix,pyDungeon_utils.find_node(my_map.nodes,my_node.connections[0][0]))
        #print("DEBUG: Connection Node "+my_node.connections[0][0])
        if my_node.room:
            current_room_number = my_node.room
            #print("We're in Room "+str(my_node.room))
            my_room = pyDungeon_utils.find_room(my_map.rooms,my_node.room)
            my_map.mask_matrix = pyDungeon_utils.unmask_room(my_map.mask_matrix,my_room)
            for temp_node in my_room.nodes:
                #print("DEBUG: Node in our room: "+temp_node)
                direction_options.append(temp_node)
                temp_node_ptr = pyDungeon_utils.find_node(my_map.nodes,temp_node)
        pyDungeon_utils.draw_dungeon(my_map,fogOfWar=True)
        im = Image.open("DemoMap.png")
        im.show()
        direction_options = list(set(direction_options))
        selection = utils.array_select_menu(direction_options,"In Room "+str(current_room_number)+". Which direction do you want to go?")
        if not selection:
            exit_now = True
        else:
            my_map.mask_matrix = pyDungeon_utils.unmask_nodes(my_map.mask_matrix,my_node,
                                    pyDungeon_utils.find_node(my_map.nodes,selection))
            my_node = pyDungeon_utils.find_node(my_map.nodes,selection)
        for proc in psutil.process_iter():
            if "eog" in proc.name():
                proc.kill()
        im.close()


if __name__ == "__main__":
    main_menu()
