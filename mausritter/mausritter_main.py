#mappa_imperium_helper.py
import utils
import dice
import dungeon
import combat
import maus_roller
import weather
import encounters
import hexmap_builder

def main_menu():     
    func_list = [dungeon.menu,combat.menu,maus_roller.menu,weather.menu,hexmap_builder.menu]
    desc_list = ["Adventure Utils","Combat Helper","Maus Creator","Weather Utils","Hexmap Builder"]
    utils.menu(func_list,desc_list,"MAUSRITTER HELPER",True)

main_menu()
