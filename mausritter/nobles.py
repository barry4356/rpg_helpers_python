#nobles.py
import dice
import nobles_tables
import creature_tables
import utils
import fileops
import additional_tables

#Noble Data Structure:
#name         - Name of noble
#race         - race of noble
#tile_located - hexmap location of noble
#mission      - mission provided by noble (random)

#Mission Data String Format (espionage)
#[name] is offering his gratitude, and [pips]pips for a favor of sorts...
#They desire [target], a [race] [descriptor] to be [mission]. 
#Target can be found in hex tile [tile], in a secret [adventure area]
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
    #TODO tile and pip calculations
    tile = dice.roll_1d20()
    pips = dice.roll_1d20() * 100
    target_name = roll_noblename()
    if not target_race:
        target_race = dice.roll_on_table(creature_tables.creatures)
    if mission_type.lower() == "bounty":
        mission_string = noble_name+" is offereing his gratitude, and "+str(pips)+"pips for a favor of sorts... "
        mission_string = mission_string+"They desire "+noble_name+", a "+target_race+" "
        mission_string = mission_string+dice.roll_on_table(additional_tables.title_table)+", to be "
        mission_string = mission_string+mission_goals+". "
        mission_string = mission_string+"Target can be found in hex tile "+str(tile)+", in a secret "
        mission_string = mission_string+dice.roll_on_table(nobles_tables.lairs)
    return mission_string

def create_noble(name="",race="",tile_located=""):
    new_noble = {}
    if not name:
        name = roll_noblename()
    if not race:
        race = dice.roll_on_table(creature_tables.creatures)
    if not tile_located:
        tile_located = dice.roll_1d20()
    mission = roll_mission(noble_name=name,tile_located=tile_located)
    new_noble["name"] = name
    new_noble["race"] = race
    new_noble["tile_located"] = tile_located
    new_noble["mission"] = mission
    write_noble(new_noble)

def noble(argv=[]):
    create_noble()