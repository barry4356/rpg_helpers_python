#contracts_tables.py
#EXPERIMENTAL
#All tables below can be added to w/o fear of breaking logic
species_table=["maus","rat","owl","faerie","ghost","centipede","spider","crow"]
title_table=["druglord","war-criminal","warlord","rogue","rebel","degenerate",
            "deviant","mogul","spy","smuggler","bully","double-crosser","turncoat","terrorist",
            "pedophile","mobster","kingpin","vagrant"]
crime_table=["mausnapping","murder","mass-murder","indecency","petty-theft","tompeepery","pip-laundering","fondling","assault","shoplifting","homicide"]

#Value between 1 and 100
#Higher value means fewer accomplices, but higher pip reward
power_level={
        "maus":10,
        "rat":15,
        "owl":50,
        "faerie":60,
        "ghost":55,
        "centipede":30,
        "spider":40,
        "crow":30
        }
