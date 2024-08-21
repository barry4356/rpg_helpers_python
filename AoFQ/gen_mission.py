#gen_mission.py

import campaign_tables
import dice
import json

def place_search_token(taken_locations):
    Location = ""
    corner = dice.coin_flip()
    location_roll = dice.roll_1d6()
    if location_roll > 4:
        Location = "In the center of any quarter, or within 6\" of any corner"
    elif corner:
        Location = "Within 6\" of corner number ["+str(location_roll)+"]"
    else:
        Location = "In the center of quarter number ["+str(location_roll)+"]"
    if Location in taken_locations:
        #No repeat locations
        return place_search_token(taken_locations)
    return Location

def place_sentries():
    Locations = []
    sentry_roll1 = dice.roll_1d4()
    sentry_roll2 = dice.roll_1d4()
    if sentry_roll1 == sentry_roll2:
        Locations = place_sentries()
        return Locations
    Locations.append("Sentry Group 1: Center of Table Quarter Number ["+str(sentry_roll1)+"]")
    Locations.append("Sentry Group 2: Center of Table Quarter Number ["+str(sentry_roll2)+"]")
    return Locations

def gen_mission(difficulty=0):
    # Roll on each table
    mission = {}
    mission['Travel Event'] = {}
    travel_roll = dice.roll_1d6() - 1
    mission['Travel Event']['Title'] = campaign_tables.travel_event[travel_roll]
    mission['Travel Event']['Description'] = campaign_tables.travel_event_desc[travel_roll]
    mission['Primary Objective'] = {}
    mission['Primary Objective']['Title'] = dice.roll_on_table(campaign_tables.primary_objectives)
    mission['Primary Objective']['Description'] = campaign_tables.primary_objectives_desc[mission['Primary Objective']['Title']]
    mission['Secondary Objective'] = {}
    mission['Secondary Objective']['Title'] = dice.roll_on_table(campaign_tables.secondary_objectives)
    mission['Secondary Objective']['Description'] = campaign_tables.secondary_objectives_desc[mission['Secondary Objective']['Title']]
    # Place Search Tokens
    mission['Search Tokens'] = {}
    mission['Search Tokens']['Count'] = dice.roll_1d3()+2
    mission['Search Tokens']['Locations'] = []
    for i in range(mission['Search Tokens']['Count']):
        mission['Search Tokens']['Locations'].append(place_search_token(mission['Search Tokens']['Locations']))
    # Place Enemy Sentries
    mission['Enemy Deployment'] = {}
    mission['Enemy Deployment']['Sentries'] = {}
    mission['Enemy Deployment']['Sentries']['Locations'] = place_sentries()

    print(json.dumps(mission,indent=2))
    return mission

gen_mission()
