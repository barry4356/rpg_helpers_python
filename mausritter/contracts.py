#contracts.py
import dice
import utils
import contracts_tables

#EXPERIMENTAL
#Used to generate random contracts

def print_contract():
    utils.print_header("WANTED (Experimental)")
    species, title, crime, reward, tile, henchmen = roll_contract()
    print("WANTED: "+species+" "+title+", for "+crime+". Reward of "+str(reward)+"pips offered.... dead or alive")
    print("Last seen in tile "+str(tile)+" with "+str(henchmen)+" accomplices")

def roll_contract():
    species = dice.roll_on_table(contracts_tables.species_table)
    title = dice.roll_on_table(contracts_tables.title_table)
    crime = dice.roll_on_table(contracts_tables.crime_table)
    henchmen = roll_henchmen(species)
    reward = roll_reward(species,henchmen)
    tile = dice.roll_1d20()
    return species, title, crime, reward, tile,henchmen

#Experimental
#The algorithm to calculate how many friends, and how much reward, is below
def roll_henchmen(species):
    power_level = contracts_tables.power_level[species]
    #Number of henchmen is capped based on species power-level
    max_henchmen = int(100 / power_level)
    return dice.roll_custom(max_henchmen+1)-1

def roll_reward(species,henchmen):
    power_level = contracts_tables.power_level[species] * (henchmen+1)
    #Reward is based on the species power level, times number of henchmen
    reward = (power_level * 20) + dice.roll_1d20()
    return reward

