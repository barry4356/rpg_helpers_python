#!/usr/bin/python

#import sys
#import os
#import time
import random
#import pandas as pd
#from datetime import date
#from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import TimeoutException

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
        print("Take turns drawing islands into your “Home Region”.)
        print("0 - Main Menu")
        print("1 - Roll")
        val = float(input("Enter Selection:"))
        
        if(val == 0):
            exit = True
        if(val == 1):
            roll = roll_1d6()
            print(island_table[roll])
            
        print()

def trun_12():
    exit = False
    while exit != True:
        print("Each player will take turns placing the results into their Home Region.")
        print("These can be placed anywhere and on any island, it is up to each player to design their own 'Home region'.")
        print("Recommended: Roll 8 times")
        print("0 - Main Menu")
        print("1 - Roll once")
        print("8 - Roll 8 times")
        val = float(input("Enter Selection:"))
        
        if(val == 0):
            exit = True
        if(val == 1):
            roll = roll_2d6()
            print(geo_table[roll])
        if(val == 8):
            for i in range(8):
                roll = roll_2d6()
                print(geo_table[roll])
        print()
    
def turn_13():
    exit = False
    while exit != True:
        print("Take turns placing 3 different resources into the player’s Home Regions.")
        print("These are up to each player to decide what to place and where.")
        print("Use a symbol to represent the resource location."
        print("These resources will help you decide where events and settlements may take place in your world.")
        print("0 - Main Menu")
              
        val = float(input("Enter Selection:"))
        
        if(val == 0):
            exit = True
        print()
              
def turn_14():
    exit = False
    while exit != True:
        print("place a capital settlement for each player's Home Region.")
        print("This is the empire each player will be devoting most of their time to throughout the rest of the game.")
        print("Be sure to create a name for your faction and design a crest to place on the map.")
        print("0 - Main Menu")
        print("1 - Roll")
        val = float(input("Enter Selection:"))
        
        if(val == 0):
            exit = True
        if(val == 1):
            roll = roll_2d6()
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
        print("0 - Main Menu")
        print("1 - Roll")
        print("2 - Roll Twice")
        val = float(input("Enter Selection:"))
        
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
        print("0 - Main Menu")
        print("1 - Roll")
        val = float(input("Enter Selection:"))
        
        if(val == 0):
            exit = True
        if(val == 1):
            roll = roll_1d6()
            print(hostile_table[roll])

              
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
        val = float(input("Enter Selection:"))
        print("\n")
        if(val == 0):
            exit = True
        
def dice_menu():
    exit = False;
    while exit != True:
        print("How many dice to roll?")
        print("1 - 1 Die")
        print("2 - 2 Dice")
        print("3 - 3 Dice")
        print("0 - Main Menu")
        val = float(input("Enter Selection:"))
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

    print("0 - Exit")
    print("1 - Take Turn")
    print("2 - Roll Dice")
    val = float(input("Enter Selection:"))
    print("\n")
    
    if(val == 0):
        print ("HERE")
        exit = True
    
    if (val == 1):
        print(turn_menu())
        
    if (val == 2):
        dice_menu()
    
#================================
