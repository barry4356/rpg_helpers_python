#nobles.py
import dice
import nobles_tables
import creature_tables
import utils
import fileops
import additional_tables
import maus_table
import hexmap_utils
import hexmath

def write_noble(new_noble):
    filename = "mausritter/data/"+new_noble["name"].replace(" ","_")+".noble"
    fileops.serialize_dict(new_noble,filename)

def roll_noblename():
    name = dice.roll_on_table(nobles_tables.nobleman_firstname)+" "+dice.roll_on_table(nobles_tables.nobleman_lastname)
    return name

def roll_mission(noble_name,mission_type="", tile_located=0,target_race=""):
    if not mission_type:
        mission_type = dice.roll_on_table(nobles_tables.mission_type)
    mission_goals = dice.roll_on_table(nobles_tables.mission_goals[mission_type])
    #TODO pip calculations
    tile = hexmap_utils.random_hex_in_area(center_tile=tile_located,max_radius=9,min_radius=3)
    pip_dist_multiplier = (hexmath.tile_distance(tile_located,tile))
    pip_travel_base = (hexmath.tile_distance(tile_located,tile)) * 350
    target_name = roll_noblename()
    if not target_race:
        target_race = dice.roll_on_table(creature_tables.creatures)
    if mission_type.lower() == "bounty":
        pip_base = (5 * additional_tables.power_level[target_race] * additional_tables.cash_multiplier) + pip_travel_base
        pips = int(pip_base + dice.roll_1d20() * 100 + dice.roll_1d20() * 10 + dice.roll_1d20())
        mission_string = noble_name+" is offereing his gratitude, and "+str(pips)+"pips for a favor of sorts...+"
        mission_string = mission_string+"They desire "+target_name+", a "+target_race+" "
        mission_string = mission_string+dice.roll_on_table(additional_tables.title_table)+", to be "
        mission_string = mission_string+mission_goals+". "
        mission_string = mission_string+"+Target can be found in hex tile "+str(tile)+", in a secret "
        mission_string = mission_string+dice.roll_on_table(nobles_tables.lairs)+".+"
        mission_string = mission_string+"Expect 1d6 Bodyguards on location."
    elif mission_type.lower() == "fetch":
        pips = int(dice.roll_custom(100) + pip_travel_base)
        mission_string = noble_name+" is offereing his gratitude, and "+str(pips)+"pips for a favor of sorts...+"
        mission_string = mission_string+"They desire the safe return of "+mission_goals+".+"
        mission_string = mission_string+"+Target can be found in hex tile "+str(tile)+", in a secret "
        mission_string = mission_string+dice.roll_on_table(nobles_tables.lairs)+"."
    return mission_string

def create_noble(name="",race="mouse",tile_located=""):
    new_noble = {}
    if not name:
        name = roll_noblename()
    if not race:
        race = dice.roll_on_table(creature_tables.creatures)
    if not tile_located:
        tile_located = dice.roll_1d20()
    mission = roll_mission(noble_name=name,tile_located=tile_located)
    appearance = dice.roll_on_table(maus_table.npc_appearance)
    quirk = dice.roll_on_table(maus_table.npc_quirk)
    new_noble["name"] = name
    new_noble["race"] = race
    new_noble["appearance"] = appearance
    new_noble["quirk"] = quirk
    new_noble["tile_located"] = tile_located
    new_noble["mission"] = mission
    new_noble["demeanor"] = "Neutral"
    print("Creating Noble: "+new_noble["name"]+" at location hex tile: "+str(new_noble["tile_located"]))
    write_noble(new_noble)

def list_nobles():
    noble_dicts = []
    nobles=fileops.get_files(path="mausritter/data",suffix=".noble")
    for filename in nobles:
        noble_dicts.append(fileops.deserialize_dict("mausritter/data/"+filename))
    nobles = list({x.replace('.noble','') for x in nobles})
    index = 0
    for noble in nobles:
        index = index+1
        noble_str=(str(index)+" - "+noble+"\tTile: "+noble_dicts[index-1]["tile_located"]).expandtabs(30)
        print(noble_str)

def delete_noble(noble_num):
    if not noble_num:
        print("ERROR: Number must be greater than zero!")
        return
    nobles=fileops.get_files(path="mausritter/data",suffix=".noble")
    nobles = list({x.replace('.noble','') for x in nobles})
    if noble_num > len(nobles):
        print("ERROR: Invalid Number (use 'noble -ls' to see list of valid numbers)")
        return
    noble_to_delete = nobles[noble_num-1]
    fileops.remove_file("mausritter/data/"+noble_to_delete+".noble")
    print("Deleted ["+noble_to_delete+"]")

def talk_noble(noble_num):
    if not noble_num:
        print("ERROR: Number must be greater than zero!")
        return
    nobles=fileops.get_files(path="mausritter/data",suffix=".noble")
    nobles = list({x.replace('.noble','') for x in nobles})
    if noble_num > len(nobles):
        print("ERROR: Invalid Number (use 'noble -ls' to see list of valid numbers)")
        return
    noble_dict = fileops.deserialize_dict("mausritter/data/"+nobles[noble_num-1]+".noble")
    utils.print_header(noble_dict["name"])
    print("Appearance: "+noble_dict["appearance"]+"\t"+"Quirk: "+noble_dict["quirk"])
    print("Demeanor: "+noble_dict["demeanor"]+"\n")
    mission_str = noble_dict["mission"]
    print(mission_str.replace("+","\n"))
    print()
    
def noble_success(noble_num=0):
    if not noble_num:
        print("ERROR: Number must be greater than zero!")
        return
    nobles=fileops.get_files(path="mausritter/data",suffix=".noble")
    nobles = list({x.replace('.noble','') for x in nobles})
    if noble_num > len(nobles):
        print("ERROR: Invalid Number (use 'noble -ls' to see list of valid numbers)")
        return
    noble_dict = fileops.deserialize_dict("mausritter/data/"+nobles[noble_num-1]+".noble")
    noble_dict["mission"] = (noble_dict["name"] + " is in debt to you. His holdings are at your disposal.")
    noble_dict["demeanor"] = "Friendly"
    write_noble(noble_dict)

def noble_failure(noble_num=0):
    if not noble_num:
        print("ERROR: Number must be greater than zero!")
        return
    nobles=fileops.get_files(path="mausritter/data",suffix=".noble")
    nobles = list({x.replace('.noble','') for x in nobles})
    if noble_num > len(nobles):
        print("ERROR: Invalid Number (use 'noble -ls' to see list of valid numbers)")
        return
    noble_dict = fileops.deserialize_dict("mausritter/data/"+nobles[noble_num-1]+".noble")
    noble_dict["mission"] = roll_mission(noble_name=noble_dict["name"],mission_type="", tile_located=noble_dict["tile_located"],target_race=noble_dict["race"])
    noble_dict["demeanor"] = "Unfriendly"
    write_noble(noble_dict)

def noble(argv=[]):
    dash_t = False 
    dash_n = 0
    dash_rm = False
    dash_talk = False
    dash_s = False
    dash_f = False
    noble_tile = 0
    noble_name = ""
    race=""
    for argument in argv:
        if argument.lower() == "-ls" or argument.lower() == "ls":
            list_nobles()
            return
        elif argument.lower() == "-rm" or argument.lower() == "rm":
            dash_rm = True
        elif argument.lower() == "-t" or "-tile" in argument.lower():
            dash_t = True
            dash_n = False
        elif argument.lower() == "-n" or "-name" in argument.lower():
            dash_n = True
        elif argument.lower() == "-talk" or argument.lower() == "talk":
            dash_talk = True
        elif argument.lower() == "-s" or "-success" in argument.lower():
            dash_s = True
        elif argument.lower() == "-f" or "-fail" in argument.lower():
            dash_f = True
        elif dash_rm:
            delete_noble(utils.to_int(argument))
            return
        elif dash_t:
            noble_tile = utils.to_int(argument)
            dash_t = False
        elif dash_talk:
            talk_noble(utils.to_int(argument))
            return
        elif dash_s:
            noble_success(utils.to_int(argument))
            return
        elif dash_f:
            noble_failure(utils.to_int(argument))
            return
        elif dash_n:
            noble_name = (noble_name+argument).replace("\"","")
            if argument[-1] == '"':
                dash_n = False
            else:
                noble_name = noble_name + " "
    if noble_tile:
        #Remove trailing space
        if noble_name[-1] == " ":
            noble_name = noble_name[:-1]
        create_noble(name=noble_name, tile_located=noble_tile)
    else:
        print("Must specify a tile (eg. noble -t 7)")