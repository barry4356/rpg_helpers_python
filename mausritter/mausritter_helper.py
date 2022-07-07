#mappa_imperium_helper.py
import utils
import dungeon
import combat
import maus_roller

def main_menu():     
    func_list = [dungeon.menu,combat.menu,maus_roller.menu]
    desc_list = ["Adventure Site Utils","Combat Helper","Maus Creator"]
    utils.menu(func_list,desc_list,"MAUSRITTER HELPER",True)

main_menu()