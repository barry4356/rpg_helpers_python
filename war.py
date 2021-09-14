#war.py
import dice
def printwar():
    print()
    print("  _    _   ___  ______  ")
    print(" | |  | | / _ \ | ___ \ ")
    print(" | |  | |/ /_\ \| |_/ / ")
    print(" | |/\| ||  _  ||    /  ")
    print(" \  /\  /| | | || |\ \  ")
    print("  \/  \/ \_| |_/\_| \_| ")
    print()
    
def war():
    printwar()
    print("OUR ARMIES APPROACH THE ENEMY SETTLEMENT! ROLL YOUR DICE!")
    input("What is the fate of our forces? Press Enter...")
    roll = dice.roll_1d6()
    print()
    if (roll == 1):
        print("Devastating Loss! Prepare for a counter attack!")
        input("Press Enter to continue...")
        print()
        war_defender()
    elif (roll == 2):
        print("The attack has failed!")
        print("Our forces are in full retreat!")
        input("Press Enter to continue...")
        print()
    elif (roll == 3):
        print("Pyrrhic victory, but victory nonetheless.")
        print("Our forces have destroyed the enemy, but the seetlement was destroyed in the process")
        input("Press Enter to continue...")
        print()
    elif (roll == 4):
        print("Attack was a success!")
        print("We have driven off the enemy and gained control of their settlement!")
        input("Press Enter to continue...")
        print()
    elif (roll == 5):
        print("Attack was a great success!")
        print("We've destroyed the enemy, taken their settlement, and even established a new fort nearby!")
        print("Place a fort near the newly-won settlement")
        input("Press Enter to continue...")
        print()
    elif (roll == 6):
        print("THE ATTACK WAS FLAWLESS!")
        print("The campaign continues on!")
        print("Place a monument to our great victory, and choose another settlement to attack!")
        input("Press Enter to continue...")
        print()
        war()
    
def war_defender():
    printwar()
    print("ENEMIES APPROACH OUR SETTLEMENT!")
    input("What is the fate of our forces? Press Enter...")
    roll = dice.roll_1d6()
    print()
    if (roll == 1):
        print("We've driven off the attackers!")
        print("Our forces run them down, and continue on to the enemy's settlement!")
        print("Choose an enemy settlement to attack!")
        input("Press Enter to continue...")
        print()
        war()
    elif (roll == 2):
        print("The enemy is rebuffed!")
        print("We've maintained control of our settlement!")
        input("Press Enter to continue...")
        print()
    elif (roll == 3):
        print("Close defeat.")
        print("Our forces were destroyed, after holding out to the last man.")
        print("The enemy have taken our settlement, but it was reduced to ruin in the process.")
        input("Press Enter to continue...")
        print()
    elif (roll == 4):
        print("We are undone!")
        print("The enemy have driven off our men and have taken our settlement!")
        input("Press Enter to continue...")
        print()
    elif (roll == 5):
        print("Attack was a terrible bloodbath!")
        print("The enemy have destroyed our forces, taken our settlement, and even established a new fort nearby!")
        print("Place a fort near the newly-lost settlement")
        input("Press Enter to continue...")
        print()
    elif (roll == 6):        
        print("THE ATTACK WAS DEVASTATING!")
        print("The enemy brough more forces to bear than expected!")
        print("NOBODY COULD HAVE FORSEEN THIS!!!!")
        print("The enemy took the settlement, placed a monument to their victory, and is now choosing another settlement to attack!")
        input("Press Enter to continue...")
        print()
        war_defender()

def war_bystander():
    printwar()
    print("THE ATTACKER APPROACHES THE DEFENDER!")
    input("Press Enter to receive battle report: ")
    roll = dice.roll_1d6()
    print()
    if (roll == 1):
        print("The attacker suffered a devastating Loss! He should prepare for a counter attack!")
        print("The attacker is now the defender!")
        input("Press Enter to continue...")
        print()
        war_bystander()
    elif (roll == 2):
        print("The attacker has failed!")
        print("Their forces are in full retreat!")
        input("Press Enter to continue...")
        print()
    elif (roll == 3):
        print("The attacker gained a pyrrhic victory.")
        print("The defending forces were destroyed...")
        print("along with the defending settlement, and a large portion of the attacker's army")
        input("Press Enter to continue...")
        print()
    elif (roll == 4):
        print("The attacker was successful!")
        print("The have driven off the defenders and gained control of the settlement!")
        input("Press Enter to continue...")
        print()
    elif (roll == 5):
        print("Attacker was greatly successful!")
        print("they've destroyed the defenders, taken their settlement, and even established a new fort nearby!")
        print("Place a fort near the newly-taken settlement")
        input("Press Enter to continue...")
        print()
    elif (roll == 6):
        print("THE ATTACK WAS FLAWLESS!")
        print("The campaign continues on!")
        print("Place a monument to the attacker's great victory, and choose another settlement to attack!")
        input("Press Enter to continue...")
        print()
        war_bystander()
