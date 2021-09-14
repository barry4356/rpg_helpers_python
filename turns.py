#turns.py

import war
import chance_tables
import dice

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
            return
        if(val == 1):
            roll = dice.roll_1d6()
            print()
            print(chanc_tables.island_table[roll])
        input("Press Enter to continue...")
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
            return
        if(val == 1):
            roll = dice.roll_2d6()
            print()
            print(chance_tables.geo_table[roll])
        if(val == 2):
            print()
            for i in range(8):
                roll = dice.roll_2d6()
                print(chance_tables.geo_table[roll])
        input("Press Enter to continue...")
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
            return
        input("Press Enter to continue...")
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
            return
        if(val == 1):
            roll = dice.roll_2d6()
            print()
            print(chanc_tables.race_table[roll])
        input("Press Enter to continue...")
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
            return
        if(val == 1):
            roll = dice.roll_1d6()
            print(chanc_tables.settlement_table[roll])
        if(val == 2):
            roll = dice.roll_1d6()
            print(chanc_tables.settlement_table[roll])
            roll = dice.roll_1d6()
            print(chanc_tables.settlement_table[roll])
        input("Press Enter to continue...")
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
            return
        if(val == 1):
            roll = dice.roll_1d6()
            print(chanc_tables.hostiles_table[roll])
            if(roll > 1 and roll < 4):
                roll = dice.roll_2d6()
                print("\t" + chanc_tables.race_table[roll])
        input("Press Enter to continue...")


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
        print()
        
        if(val == 0):
            exit = True
            return
        if(val == 1):
            roll = dice.roll_3d6()
            turn_41_helper(roll)
        if(val == 2):
            for i in range(7):
                roll = dice.roll_3d6()
                turn_41_helper(roll)
                print()
        input("Press Enter to continue...")


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
        roll2 = dice.roll_2d6()
        print("\t" + chanc_tables.geo_table[roll2])
        roll2 = dice.roll_2d6()
        print("\t" + chanc_tables.geo_table[roll2])
    elif(roll == 6):
        print("Your scouts report back a mysterious ruin. Draw in a monolith, henge, or ruined site.")
    elif(roll == 7):
        print("Scouts reported back new and terrifying lands. Place the geography:")
        roll2 = dice.roll_2d6()
        print("\t" + chanc_tables.geo_table[roll2])
    elif(roll == 8):
        print("Brigands have been spotted nearby")
        print("Place a new hostile settlement on a trade route or bay, then give them a name and banner.")
    elif(roll == 9):
        print("Your explorers have made contact with a primitive tribe.")
        print("place a new tribe settlement of race:")
        roll2 = dice.roll_2d6()
        print("\t" + chanc_tables.race_table[roll2])
    elif(roll == 10):
        print("Your empire is growing to distant shores.")
        print("Build a new coastal settlement, preferably on a nearby island.")
    elif(roll == 11):
        print("Your empire is expanding.")
        print("Place a new settlement near an existing one. settlement type:")
        roll2 = dice.roll_1d6()
        print("\t" + chanc_tables.settlement_table[roll2])
    elif(roll == 12):
        print("Scouts have discovered another kingdom!")
        print("Place 2 settlements. Faction's Race:")
        roll2 = dice.roll_2d6()
        print("\t" + chanc_tables.race_table[roll2])
    elif(roll == 13):
        print("A nearby hostile force has attacked!")
        print("destroy a fort or settlement and replace it with a ruin, or claim it for the new invaders.")
    elif(roll == 14):
        print("Choose one neighboring faction and roll to add a settlement for them.")
    elif(roll == 15):
        print("Your Explorers have discovered a valuable new resource! Place a new resource symbol, distant from your Capital.")
    elif(roll == 16):
        print("Strange and magnificent beasts have been spotted. Are they terrifyingly large, aggressive, tasty? Draw in a symbol and name for these new creatures.")
    elif(roll == 17):
        print("Scouts have stumbled upon an impressive landmark, is it a strange rock formation, a lone monolith, magical grove?")
        print("Draw it in now.")
    elif(roll == 18):
        print("Your scouts have disturbed and awakened a legendary monster, draw in a new monster and give it a name.")
            
def turn_neighbors_expand():
          
    exit = False
    while exit != True:
        print("Each player takes turns choosing one neighbor within their home region and places an additional settlement for them.") 
        print("You can choose what to place for the civilized neighbors, claim a ruin, or place a new camp for a tribe, cult, etc.")
        print("0 - Back")
        val = float(input("Enter Selection: "))
        print()
        
        if(val == 0):
            exit = True

            
def turn_51():
    
    print("Your empires have gained a foothold and perhaps even expanded onto neighboring islands.")
    print("Now it’s time to flex their might and expand, or perhaps fight, their way across the seas.")
    exit = False
    while exit != True:
        print("All results can now be placed in any region on the map.")
        print("Roll 7 times in this Era for 70 years of advancement.")
        print("0 - Back")
        print("1 - Roll once")
        print("2 - Roll 7 times")
        val = float(input("Enter Selection: "))
        print()
        
        if(val == 0):
            exit = True
            return
        if(val == 1):
            roll = dice.roll_3d6()
            turn_51_helper(roll)
        if(val == 2):
            for i in range(7):
                roll = dice.roll_3d6()
                turn_51_helper(roll)
                print()
        input("Press Enter to continue...")
        print()
         
def turn_51_helper(roll):
    if(roll == 3):
        print("Tourism - Is it a beautiful waterfall, mana spring, or enchanted grove?")
        print("Your empire has built a new settlement on/near this site.")
    elif(roll == 4):
        print("One of your settlements has grown tired of your rule and thrown out the ruling class.")
        print("Rename this new 'free' city and give the new faction a name and banner.")
    elif(roll == 5):
        print("One of your settlements is rapidly growing.")
        print("Grow one of your smaller villages into a city by adding more buildings, placing farmland, adding 'city' to the end of the name, etc.")
    elif(roll == 6):
        print("A powerful hero has shown up in the Empire, what did they do?")
        print("Draw in a statue or monument near your capital or the location of the event.")
    elif(roll == 7):
        print("A nearby hostile force has attacked!")
        print("Destroy a fort or settlement and replace it with a ruin, or claim it for the new invaders.")
    elif(roll == 8):
        print("Your army is marching!") 
        print("Select any settlement not already owned by you and prepare for War!")
        input("Are you prepared for WAR?!: ")
        war.war()
    elif(roll == 9):
        print("Some of your people have set out on their own.")
        print("Place a new Faction onto the map (be sure to give them a banner and name)")
        print("Settlement type: ")
        roll2 = dice.roll_1d6()
        print("\t" + chanc_tables.settlement_table[roll2])
    elif(roll == 10):
        print("Your military strength is growing, draw in either a new frontier fort or add city walls to an existing settlement.")
        print("(City walls will crumble instead of a city during an attack)")
    elif(roll == 11):
        print("Your empire is growing!")
        print("Place a new settlement anywhere on the map.")
        print("Settlement Type:")
        roll2 = dice.roll_1d6()
        print("\t" + chanc_tables.settlement_table[roll2])
    elif(roll == 12):
        print("People are flocking to your empire.")
        print("Grow your cities if possible, add more farmland, draw ships in the ports, etc.")
    elif(roll == 13):
        print("Economic Prosperity!")
        print("Build a road connecting your empire to another faction, then add a trade post somewhere along the road.")
        print("(consider resource locations)")
        print("If no possible road connections exist, build a new coastal trade post")
    elif(roll == 14):
        print("Something nefarious is looming in your empire and has gathered enough worshipers to construct its own facility.")
        print("Demon summoners, necromancers, mad wizards, it’s up to you.") 
        print("Draw in an appropriate building for the cult/organization.")
    elif(roll == 15):
        print("Something terrible has struck the empire.")
        print("Natural Disaster or Magical, famine or disease?") 
        print("Remove a settlement and replace it with a ruin..")
    elif(roll == 16):
        print("Your empire has cultivated a new craft, art, or ability.") 
        print("Are they spellcasters, researchers, monks, druids?") 
        print ("Build a new academy for this group and place this new settlement.")
    elif(roll == 17):
        print("Your growing empire needs food!")
        print("Place either a new farming town or fishing village")
    elif(roll == 18):
        print("Rebellion!") 
        print("Half your empire has split into a new faction.") 
        print("Give them a name and banner, and treat them as a hostile neighbor from now on.")
                        
def turn_61():
    
    print("With every rising empire there is a falling one.")
    print("Open land is quickly diminishing and with that, wars, famine, & rebellion become a common occurrence.")
    exit = False
    while exit != True:
        print("Take 6 turns in this era for 60 years of story.")
        print("All results can be placed anywhere on the map")
        print("0 - Back")
        print("1 - Roll once")
        print("2 - Roll 6 times")
        val = float(input("Enter Selection: "))
        print()
        
        if(val == 0):
            exit = True
            return
        if(val == 1):
            roll = dice.roll_3d6()
            turn_61_helper(roll)
        if(val == 2):
            for i in range(6):
                roll = dice.roll_3d6()
                turn_61_helper(roll)
                print()
        input("Press Enter to continue...")

        print()

def turn_61_helper(roll):
    if(roll == 3):
        print("A Monster has risen from underground and destroyed or claimed one of your settlements.")
        print("Place a new monster on the map now (don’t forget a name)")
    elif(roll == 4):
        print("Has a portal to a new realm opened, or perhaps a mad wizard has crafted a new tower?")
        print("Describe & draw in a magical occurrence, anything from a new tower to a massive crater.")
    elif(roll == 5):
        print("Many heroes have given their lives for your kingdom.")
        print("Draw in a monument or statue near your capital or place of importance.")
    elif(roll == 6):
        print("Your rulers need a place to live!")
        print("Build a palace for them near the capital or somewhere of importance")
    elif(roll == 7):
        print("Your people think they can have a better life outside your empire.")
        print("Remove one of your settlements and place a new one somewhere on the map.")
        print("Be sure to give them a new faction name and banner.")
    elif(roll == 8):
        print("Despite the times, your empire is thriving!") 
        print("Either expand an existing settlement with farmland, walls, etc.")
        print("Or create a new settlement of type:")
        roll2 = dice.roll_1d6()
        print("\t" + chanc_tables.settlement_table[roll2])
    elif(roll == 9):
        print("Something terrible has struck the empire.")
        print("Natural Disaster or Magical, famine or disease?")
        print("Remove a settlement and replace it with a ruin")
    elif(roll == 10):
        print("Your army is marching!") 
        print("Select any settlement not already owned by you and prepare for War!")
        input("Are you prepared for WAR?!: ")
        war.war()
    elif(roll == 11):
        print("You have been attacked!!")
        print("Destroy a fort, city wall, or settlement and replace it with a ruin.")
    elif(roll == 12):
        print("Choose one hostile neighbor and add a settlement for them of type:")
        roll2 = dice.roll_1d6()
        print("\t" + chanc_tables.settlement_table[roll2])
    elif(roll == 13):
        print("Select any two neighboring factions.")
        print("choose which is the attacker and defender, then prepare for War!")
        input("Are they prepared for WAR?!: ")
        war.war_bystander()
    elif(roll == 14):
        print("Something sinister has claimed a nearby ruin.")
        print("Place a new cult or evil force onto the map on an existing ruin.") 
        print("(If no empty ruin exists, find an empty place on the map for them)")
    elif(roll == 15):
        print("A Minor Faction has joined your empire.")
        print("Create an Alliance Banner and give your new United Kingdom a name.") 
    elif(roll == 16):
        print("People are flocking to your city, are they fleeing war, monster attacks, disasters?") 
        print("Place a small village next to or expand your capital for these new citizens.")
    elif(roll == 17):
        print("Something fowl is lurking in the forest (or any geography) is it lycanthropy, demonic spiders, a mad druid?")
        print("Treat them as a hostile faction and give the location an ominous name")
    elif(roll == 18):
        print("Rebellion!") 
        print("Half your empire has split into a new faction.") 
        print("Give them a name and banner, and treat them as a hostile neighbor from now on.")
