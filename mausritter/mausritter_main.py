#mappa_imperium_helper.py
import utils
import dice
import dungeon
import combat
import maus_roller
import weather
import encounters

def main_menu():     
    func_list = [dungeon.menu,combat.menu,maus_roller.menu,weather.menu,encounters.adventure_generator]
    desc_list = ["Adventure Site Utils","Combat Helper","Maus Creator","Weather Utils","Random Adventure"]
    utils.menu(func_list,desc_list,"MAUSRITTER HELPER",True)

main_menu()