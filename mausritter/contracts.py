#contracts.py
import dice
import utils
import additional_tables
import random

#EXPERIMENTAL
#Used to generate random contracts

def print_contract(min_tile=1,max_tile=20):
    utils.print_header("WANTED (Experimental)")
    species, title, crime, reward, tile, henchmen = roll_contract(min_tile,max_tile)
    print("WANTED: "+species+" "+title+", for "+crime+". Reward of "+str(reward)+"pips offered.... dead or alive")
    print("Last seen in tile "+str(tile)+" with "+str(henchmen)+" accomplices")

def roll_contract(min_tile=1,max_tile=20):
    species = dice.roll_on_table(additional_tables.species_table)
    title = dice.roll_on_table(additional_tables.title_table)
    crime = dice.roll_on_table(additional_tables.crime_table)
    henchmen = roll_henchmen(species.lower())
    reward = roll_reward(species.lower(),henchmen)
    tile = random.randint(min_tile,max_tile)
    return species, title, crime, reward, tile,henchmen

#Experimental
#The algorithm to calculate how many friends, and how much reward, is below
def roll_henchmen(species):
    power_level = additional_tables.power_level[species]
    #Number of henchmen is capped based on species power-level
    max_henchmen = utils.round(100 / power_level)
    return dice.roll_custom(max_henchmen+1)-1

#Reward is based on the species power level, times number of henchmen
def roll_reward(species,henchmen):
    power_level = additional_tables.power_level[species] * (henchmen+1)
    reward = (power_level * additional_tables.cash_multiplier)
    #Add a random bonus on top of the base reward
    reward = dice.roll_custom(reward) + reward
    return reward

def wanted(argv=[]):
    if len(argv) >= 2:
        try:
            min_tile=int(argv[0])
            max_tile=int(argv[1])
        except ValueError:
            min_tile = 1
            max_tile = 20
        if min_tile <= max_tile:
            print_contract(min_tile, max_tile)
        else:
            print_contract()
    else:
        print_contract()
    print()
