#hexmap_builder.py
import hexmap_builder_tables
import dice
import utils

def rnp_settlement():
    inhabitants, size, feature, governance, industry, event, name, tavern_name, tavern_specialty = roll_settlement()
    print_settlement(inhabitants, size, feature, governance, industry, event, name, tavern_name, tavern_specialty)

def roll_settlement():
    tavern_name = ""
    tavern_specialty = ""
    inhabitants = dice.roll_on_table(hexmap_builder_tables.settlement_inhabitants)
    feature = dice.roll_on_table(hexmap_builder_tables.settlement_feature)
    size_roll = dice.roll_1d6()
    size = hexmap_builder_tables.settlement_size[size_roll-1]
    gov_roll = dice.roll_1d6() + size_roll
    governance = hexmap_builder_tables.settlement_governance[gov_roll-1]
    industry = dice.roll_on_table(hexmap_builder_tables.settlement_industry)
    event = dice.roll_on_table(hexmap_builder_tables.settlement_event)
    name = (dice.roll_on_table(hexmap_builder_tables.settlement_nameA) + 
        dice.roll_on_table(hexmap_builder_tables.settlement_nameB))
    #Taverns only in hamlet or larger
    if size_roll > 2:
        tavern_name = (dice.roll_on_table(hexmap_builder_tables.tavern_nameA) + 
            dice.roll_on_table(hexmap_builder_tables.tavern_nameB))
        tavern_specialty = dice.roll_on_table(hexmap_builder_tables.tavern_specialty)
    return inhabitants, size, feature, governance, industry, event, name, tavern_name, tavern_specialty

def roll_hex():
    hex_type = dice.roll_on_table(hexmap_builder_tables.hex_type)
    if "countryside" in hex_type.lower():
        landmark = dice.roll_on_table(hexmap_builder_tables.countryside_landmarks)
    elif "forest" in hex_type.lower():
        landmark = dice.roll_on_table(hexmap_builder_tables.forest_landmarks)
    elif "river" in hex_type.lower():
        landmark = dice.roll_on_table(hexmap_builder_tables.river_landmarks)
    elif "humantown" in hex_type.lower():
        landmark = dice.roll_on_table(hexmap_builder_tables.humantown_landmarks)
    else:
        landmark = "N/A"
        print("ERROR: Invalid Hex Type... WTF")
    if dice.roll_1d6() == 1:
        settlement_present = True
    else:
        settlement_present = False
    #If settlement_present on hex; we need to pull the settlement's details separately
    details = ""
    if not settlement_present:
        details = dice.roll_on_table(hexmap_builder_tables.landmark_details)
    return hex_type, landmark, details, settlement_present

def print_settlement(inhabitants, size, feature, governance, industry, event, name, tavern_name, tavern_specialty):
    utils.print_header(name)
    print("Inhabitants: "+inhabitants+"\tSize: "+size)
    print("Governance: "+governance)
    print("Industry: "+industry)
    if tavern_name:
        print("Tavern: "+tavern_name+"\tSpecialty: "+tavern_specialty)
    print("Notable Feature: "+feature)
    print("Event: "+event)

def print_hex():
    hex_type, landmark, details, settlement_present = roll_hex()
    utils.print_header("New Hex")
    print("Hex Type: "+hex_type+"\tLandmark: "+landmark)
    if not settlement_present:
        print("Details: "+details)
    else:
        inhabitants, size, feature, governance, industry, event, name, tavern_name, tavern_specialty = roll_settlement()
        print("Settlement present: "+name)
        print_settlement(inhabitants, size, feature, governance, industry, event, name, tavern_name, tavern_specialty)

def menu():
    func_list = [print_hex,rnp_settlement]
    desc_list = ["Create New Hex","Roll New Settlement"]
    utils.menu(func_list,desc_list,"Adventure Menu",False)