
import random
import turns
import war

#============= Chance Tables =============
island_table = ["N/A", "1 large continent", "1 large + 1 small island", "1 large + 2 small islands", "2 medium islands", "3 medium islands", "4 small islands"]
geo_table = ["N/A", "N/A", "Savanna",  "Wetlands", "Hills", "Lake", "River", "Forest", "Mountains", "Desert", "Jungle", "Canyon", "Volcano"]
race_table = ["N/A", "N/A", "Demonkind", "Seafolk", "Smallfolk", "Reptilian", "Dwarves", "Humans", "Elves", "Greenskins", "Animalfolk", "Giantkind", "Player’s choice"]
number_of_gods = [0, 1, 2, 2, 3, 3, 4]
god_domain_table = [ "N/A", "A Geography", "Something in Nature", "A Craft or Art", "An Endeavor", "Something around the home", "Something Grim"]
god_symbol_table = ["N/A", "Weapon", "Tool", "Animal", "Plant", "Natural", "Body Part"]
settlement_table = ["N/A", "Farming Village", "Mining Settlement", "Resource Town", "Trade Post / Market Hub", "Frontier / Military Fort", "Monastery / Temple"]
hostiles_table = ["N/A", "Insect Hive", "Hostile Tribe", "Minor Faction", "Necromancer / Mad Mage", "Demon Lair", "Legendary Monster"]
#================================

#============= UTILS =============
def roll_1d6():
    return (random.randrange(6) + 1)
    
def roll_2d6():
    val = roll_1d6() + roll_1d6()
    return (val)
    
def roll_3d6():
    val = roll_1d6() + roll_1d6() + roll_1d6()
    return (val)



#=================================
#============= Menus =============       
def turn_menu():
    exit = False;
    while exit != True:
        print("Please input either a turn number, or menu selection...")
        print("1.1: Island Creation")
        print("1.2: Geography")
        print("1.3: Resources")
        print("1.4: Major Faction")
        #print("2.1: Number of Gods")
        #print("2.2: Domains")
        #print("2.3: Symbol")
        #print("2.4: Name")
        print("3.1: Early Settlers")
        print("3.2: Hostile Neighbors")
        print("4.1: Exploration Begins")
        print("4.2: Neighbor Expansion")
        print("5.1: Worldwide Expansion")
        print("5.2: Neighbor Expansion")
        print("6.1: Final Era")
        print("6.2: Neighbor Expansion")
        print("6.3: Finalizing")
        print("0 - Main Menu")
        val = float(input("Enter Selection: "))
        print("\n")
        if(val == 0):
            exit = True
        elif(val == 1.1):
            turns.turn_11()
        elif(val == 1.2):
            turns.turn_12()
        elif(val == 1.3):
            turns.turn_13()
        elif(val == 1.4):
            turns.turn_14()
        elif(val == 3.1):
            turns.turn_31()
        elif(val == 3.2):
            turns.turn_32()
        elif(val == 4.1):
            turns.turn_41()
        elif(val == 4.2 or val == 5.2 or val == 6.2):
            turns.turn_neighbors_expand()
        elif(val == 5.1):
            turns.turn_51()
        elif(val == 6.1):
            turns.turn_61()
        
        
def dice_menu():
    exit = False;
    while exit != True:
        print("How many dice to roll?")
        print("1 - 1 Die")
        print("2 - 2 Dice")
        print("3 - 3 Dice")
        print("0 - Main Menu")
        val = float(input("Enter Selection: "))
        print()
        if(val == 0):
            exit = True
        elif(val == 1):
            print(roll_1d6())
        elif(val == 2):
            print(roll_2d6())
        elif(val == 3):
            print(roll_3d6())
        print()
        
def war_menu():
    exit = False;
    while exit != True:
        print("Which type of war?")
        print("1 - War (Attacker)")
        print("2 - War (Defender)")
        print("3 - War (Generic)")
        print("0 - Main Menu")
        val = float(input("Enter Selection: "))
        print()
        if(val == 0):
            exit = True
            return
        elif(val == 1):
            war.war()
        elif(val == 2):
            war.war_defender()
        elif(val == 3):
            war.war_bystander()
        print()
#=====================================
#============= MAIN MENU =============
print ("\n===== MAPPA IMPERIUM HELPER =====\n")
exit = False;
while exit != True:
    print("Menu Selection...")

    print("1 - Take Turn")
    print("2 - Roll Dice")
    print("3 - War")
    print("0 - Exit")
    
    val = float(input("Enter Selection: "))
    print("\n")
    
    if(val == 0):
        exit = True
    elif (val == 1):
        print(turn_menu())
    elif (val == 2):
        dice_menu()
    elif (val == 3):
        war_menu()
#================================
