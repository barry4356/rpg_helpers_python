#!/usr/bin/python

import random

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
#================================

def turn_11():
    print("Mountains rise, forests grow. Small settlements begin to form, including an empire for each player to develop throughout the course of the game.");
    print("During this stage of the game, each player will take turns drawing out the islands, geography, factions, and resources in their 'Home Region'")
    print("")
    
    exit = False
    while exit != True:
        print("Take turns drawing islands into your 'Home Region'.")
        print("0 - Back")
        print("1 - Roll")
        val = float(input("Enter Selection: "))
        
        if(val == 0):
            exit = True
        if(val == 1):
            roll = roll_1d6()
            print()
            print(island_table[roll])
            
        print()

def turn_12():
    exit = False
    while exit != True:
        print("Each player will take turns placing the results into their Home Region.")
        print("These can be placed anywhere and on any island, it is up to each player to design their own 'Home region'.")
        print("0 - Back")
        print("1 - Roll once")
        print("2 - Roll 8 times")
        val = float(input("Enter Selection: "))
        
        if(val == 0):
            exit = True
        if(val == 1):
            roll = roll_2d6()
            print()
            print(geo_table[roll])
        if(val == 2):
            print()
            for i in range(8):
                roll = roll_2d6()
                print(geo_table[roll])
        print()
    
def turn_13():
    exit = False
    while exit != True:
        print("Take turns placing 3 different resources into the player’s Home Regions.")
        print("These are up to each player to decide what to place and where.")
        print("Use a symbol to represent the resource location.")
        print("These resources will help you decide where events and settlements may take place in your world.")
        print("0 - Back")
              
        val = float(input("Enter Selection: "))
        
        if(val == 0):
            exit = True
        print()
              
def turn_14():
    exit = False
    while exit != True:
        print("place a capital settlement for each player's Home Region.")
        print("This is the empire each player will be devoting most of their time to throughout the rest of the game.")
        print("Be sure to create a name for your faction and design a crest to place on the map.")
        print("0 - Back")
        print("1 - Roll")
        val = float(input("Enter Selection: "))
        
        if(val == 0):
            exit = True
        if(val == 1):
            roll = roll_2d6()
            print()
            print(race_table[roll])

        print()

def turn_31():
    print("The lands have been drawn and each empire now has a starting settlement.")
    print("This era will develop your faction settlements in small empires.") 
    print("This era consists of the first 50 years of your empire’s story.")
          
    exit = False
    while exit != True:
        print("placing new settlements for their empire.")
        print("These must all be placed on the same island as their capital.")
        print("Be sure to name and connect each settlement with a road (a dotted line works well to represent this)")
        print("Roll twice for each player")
        print("0 - Back")
        print("1 - Roll")
        print("2 - Roll Twice")
        val = float(input("Enter Selection: "))
        print()
        
        if(val == 0):
            exit = True
        if(val == 1):
            roll = roll_1d6()
            print(settlement_table[roll])
        if(val == 2):
            roll = roll_1d6()
            print(settlement_table[roll])
            roll = roll_1d6()
            print(settlement_table[roll])
              
        print()
           
def turn_32():
    exit = False
    while exit != True:
        print("Each player takes turns rolling on the Hostiles Table to select their hostile neighbors, then places them anywhere in their home region.")
        print("Give them a name and draw in an appropriate symbol to designate their location. (Small camp, tower, dragon, etc)")
        print("0 - Back")
        print("1 - Roll")
        val = float(input("Enter Selection: "))
        print()
        
        if(val == 0):
            exit = True
        if(val == 1):
            roll = roll_1d6()
            print(hostiles_table[roll])
            if(roll > 1 and roll < 4):
                roll = roll_2d6()
                print("\t" + race_table[roll])

        print()
            
def turn_41():
          
    exit = False
    while exit != True:
        print("Each player will take turns exploring their nearby islands.")
        print("All results can be placed anywhere within each player's Home Region.")
        print("Roll 7 times on this table.")
        print("0 - Back")
        print("1 - Roll once")
        print("2 - Roll 7 times")
        val = float(input("Enter Selection: "))
        
        if(val == 0):
            exit = True
        if(val == 1):
            roll = roll_3d6()
            turn_41_helper(roll)
        if(val == 2):
            for i in range(7):
                roll = roll_3d6()
                turn_41_helper(roll)
                print()

        print()
    
def turn_41_helper(roll):
    if(roll == 3):
        print("Something magical, powerful, or otherworldly has been discovered.")
        print("Describe and draw this relic, be sure to give it, and if necessary the location, a name.")
    elif(roll == 4):
        print("Sinister forces are lurking.")
        print("Is it demons, twisted abominations, bloodthirsty spiders?")
        print("Draw in this new hostile neighbor with an appropriate settlement")
    elif(roll == 5):
        print("Your sea explorers have discovered a new island! Draw in 1 small island, with geography:")
        roll2 = roll_2d6()
        print("\t" + geography_table(roll2))
        roll2 = roll_2d6()
        print("\t" + geography_table(roll2))
    elif(roll == 6):
        print("Your scouts report back a mysterious ruin. Draw in a monolith, henge, or ruined site.")
    elif(roll == 7):
        print("Scouts reported back new and terrifying lands. Place the geography:")
        roll2 = roll_2d6()
        print("\t" + geography_table(roll2))
    elif(roll == 8):
        print("Brigands have been spotted nearby")
        print("Place a new hostile settlement on a trade route or bay, then give them a name and banner.")
    elif(roll == 9):
        print("Your explorers have made contact with a primitive tribe.")
        print("place a new tribe settlement of race:")
        roll2 = roll_2d6()
        print("\t" + race_table[roll2])
    elif(roll == 10):
        print("Your empire is growing to distant shores.")
        print("Build a new coastal settlement, preferably on a nearby island.")
    elif(roll == 11):
        print("Your empire is expanding.")
        print("Place a new settlement near an existing one. settlement type:")
        roll2 = roll_1d6()
        print("\t" + settlement_table[roll2])
    elif(roll == 12):
        print("Scouts have discovered another kingdom!")
        print("Place 2 settlements. Faction's Race:")
        roll2 = roll_2d6()
        print("\t" + race_table[roll2])
    elif(roll == 13):
        print("A nearby hostile force has attacked!")
        print("destroy a fort or settlement and replace it with a ruin, or claim it for the new invaders.")
    elif(roll == 14):
        print()
    elif(roll == 15):
        print()
    elif(roll == 16):
        print()
    elif(roll == 17):
        print()
    elif(roll == 18):
        print()
              
def turn_menu():
    exit = False;
    while exit != True:
        print("Please input either a turn number, or menu selection...")
        print("1.1: Island Creation")
        print("1.2: Geography")
        print("1.3: Resources")
        print("1.4: Major Faction")
        print("2.1: Number of Gods")
        print("2.2: Domains")
        print("2.3: Symbol")
        print("2.4: Name")
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
        if(val == 1.1):
            turn_11()
        if(val == 1.2):
            turn_12()
        if(val == 1.3):
            turn_13()
        if(val == 1.4):
            turn_14()
        if(val == 3.1):
            turn_31()
        if(val == 3.2):
            turn_32()
        
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
        if(val == 1):
            print(roll_1d6())
        if(val == 2):
            print(roll_2d6())
        if(val == 3):
            print(roll_3d6())
        print()
            
#============= MAIN MENU =============

print ("\n===== MAPPA IMPERIUM HELPER =====\n")
exit = False;
while exit != True:
    print("Menu Selection...")

    print("1 - Take Turn")
    print("2 - Roll Dice")
    print("0 - Exit")
    
    val = float(input("Enter Selection: "))
    print("\n")
    
    if(val == 0):
        exit = True
    
    if (val == 1):
        print(turn_menu())
        
    if (val == 2):
        dice_menu()
    
#================================
