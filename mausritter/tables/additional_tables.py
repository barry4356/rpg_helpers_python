#additional_tables.py

#Pulled from Proposed Additional Rules (Experimental)

large=["cat","snake","snake","crow","crow","owl"]
medium=[
    "frog w/ d10 spear","frog w/ d10 spear","frog w/ d10 spear",
    "centipede","ghost","faerie w/ d8 Silver Rapier"
]
small=[
    "mouse w/ d6 sword","mouse w/ d8 Bow","mouse w/ d6 sword","mouse w/ d8 Bow","rat w/ d6 cleaver",
    "rat w/ d6 cleaver","rat w/ d6 cleaver","rat w/ d6 cleaver","rat w/ d6 cleaver","rat w/ d6 cleaver"
]
tiny=["spider","spider","spider","centipede","centipede","centipede"]

#EXPERIMENTAL -  CONTRACTS TABLES
#All tables below can be added to w/o fear of breaking logic
species_table=[
    "Maus","Rat","Owl","Faerie","Ghost","Centipede","Spider","Crow","Frog","Snake"
]
title_table=[
    "druglord","war-criminal","warlord","rogue","rebel","degenerate",
    "deviant","mogul","spy","smuggler","bully","double-crosser",
    "turncoat","terrorist","pedophile","mobster","kingpin","vagrant","deserter"
]
crime_table=[
    "mausnapping","murder","mass-murder","indecency","petty-theft",
    "tompeepery","pip-laundering","fondling","assault","shoplifting",
    "homicide","skulduggery","tax-evasion","mausslaughter","rabbit-rustling",
    "rabble-rousing"
]
#Value between 1 and 100 (horde sized enemies are higher)
#Higher value means fewer accomplices, but higher pip reward:
# Max number of accomplices = 100 / power_level
# Min Pips per head = power_level * cash_multiplier
# Max Pips per head = 2 * (power_level * cash_multiplier)
power_level={
    "maus":10,
    "rat":15,
    "frog":20,
    "owl":100,
    "faerie":75,
    "ghost":75,
    "centipede":30,
    "spider":40,
    "crow":30,
    "snake":50,
    "cat":400
}
cash_multiplier = 10
