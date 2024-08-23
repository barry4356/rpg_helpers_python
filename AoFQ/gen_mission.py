#gen_mission.py

import campaign_tables
import dice
import json
import argparse

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

def gen_mission(difficulty, use_legacy, use_current, use_narrative):
    # Roll on each table
    mission = {}
    mission['Travel Event'] = {}
    travel_roll = dice.roll_1d6() - 1
    mission['Travel Event']['Title'] = campaign_tables.travel_event[travel_roll]
    mission['Travel Event']['Description'] = campaign_tables.travel_event_desc[travel_roll]
    mission['Primary Objective'] = {}
    primary_obj_table = []
    if (use_legacy):
        primary_obj_table.extend(campaign_tables.primary_objectives_legacy)
    if (use_current):
        primary_obj_table.extend(campaign_tables.primary_objectives)
    if (use_narrative):
        primary_obj_table.extend(campaign_tables.primary_objectives_narrative)
    mission['Primary Objective']['Title'] = dice.roll_on_table(primary_obj_table)
    mission['Primary Objective']['Description'] = campaign_tables.primary_objectives_desc[mission['Primary Objective']['Title']]
    mission['Secondary Objective'] = {}
    secondary_obj_table = []
    if (use_legacy):
        secondary_obj_table.extend(campaign_tables.secondary_objectives_legacy)
    if (use_current):
        secondary_obj_table.extend(campaign_tables.secondary_objectives)
    if (use_narrative):
        secondary_obj_table.extend(campaign_tables.secondary_objectives_narrative)
    mission['Secondary Objective']['Title'] = dice.roll_on_table(secondary_obj_table)
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

PARSER = argparse.ArgumentParser(description='Generate \'Age of Fantasy: Quest\' Mission')
PARSER.add_argument('-a', '--all', action='store_true', help='Pull options from all available sources', required=False)
PARSER.add_argument('-l', '--legacy', action='store_true', help='Pull options from legacy rulebooks', required=False)
PARSER.add_argument('-c', '--current', action='store_true', help='Pull options from current rulebook', required=False)
PARSER.add_argument('-n', '--narrative', action='store_true', help='Pull options from narrative rulebook', required=False)
#Default to current rulebook only; if 'all' specified use all rulebooks; if legacy/narrative specified, use args to decide
args = PARSER.parse_args()
use_legacy = False
use_current = True
use_narrative = False
if args.all:
    use_legacy = True
    use_current = True
    use_narrative = True
elif args.legacy or args.narrative:
    use_legacy = args.legacy
    use_current = args.current
    use_narrative = args.narrative

#Generate mission
gen_mission(0, use_legacy, use_current, use_narrative)
