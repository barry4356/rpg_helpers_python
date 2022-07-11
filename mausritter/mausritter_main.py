#mappa_imperium_helper.py
import utils
import dice
import dungeon
import combat
import maus_roller
import weather
import random_adventure_table

def adventure_generator():
    utils.print_header("Generated Adventure")
    creature_str = dice.roll_on_table(random_adventure_table.creature)
    problem_str = dice.roll_on_table(random_adventure_table.problem)
    complication_str = dice.roll_on_table(random_adventure_table.complication)
    print("The adventurers find a ["+creature_str+"] who ["+problem_str+"]. Unfortunately ["+complication_str+"].")
    print("Can our brave mice sally forth to solve this dilema?")

def main_menu():     
    func_list = [dungeon.menu,combat.menu,maus_roller.menu,weather.menu,adventure_generator]
    desc_list = ["Adventure Site Utils","Combat Helper","Maus Creator","Weather Utils","Random Adventure"]
    utils.menu(func_list,desc_list,"MAUSRITTER HELPER",True)

main_menu()