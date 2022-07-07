#mappa_imperium_helper.py
import dice
import utils
import dungeon
import combat

def main_menu():     
    func_list = [dungeon.menu,combat.menu]
    desc_list = ["Adventure Site Utils","Combat Helper"]
    utils.menu(func_list,desc_list,"MAUSRITTER HELPER",True)

main_menu()