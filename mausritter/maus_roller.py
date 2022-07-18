#maus_roller.py
#Use this to roll some Mice
import dice
import maus_table
import utils

def get_stats(is_pc=False):
    #If player-character, roll 3d6 and drop lowest
    if is_pc:
        strength = dice.roll_3d6_keep2()
        dex = dice.roll_3d6_keep2()
        wil = dice.roll_3d6_keep2()
    else:
        strength = dice.roll_2d6()
        dex = dice.roll_2d6()
        wil = dice.roll_2d6()
    hp = dice.roll_1d6()
    return strength, dex, wil, hp


def get_mausname():
    first_name = dice.roll_on_table(maus_table.birthname)
    last_name = dice.roll_on_table(maus_table.matriname)
    return str(first_name+" "+last_name)

def get_details():
    birthsign_num = dice.roll_1d6()-1
    birthsign = maus_table.birthsign[birthsign_num]
    disposition = maus_table.disposition[birthsign_num]
    coat = maus_table.coat[dice.roll_1d6()-1]
    pattern = maus_table.pattern[dice.roll_1d6()-1]
    physical_detail = maus_table.physical_detail[dice.roll_1d6()-1]
    return birthsign, disposition, coat, pattern, physical_detail

def get_npc_appearance():
    status = dice.roll_on_table(maus_table.npc_status)
    appearance = dice.roll_on_table(maus_table.npc_appearance)
    quirk = dice.roll_on_table(maus_table.npc_quirk)
    wants = dice.roll_on_table(maus_table.npc_wants)
    relationship = dice.roll_on_table(maus_table.npc_relationship)
    return status, appearance, quirk, wants, relationship

def roll_main_character():
    hp = roll_henchman(is_pc=True)
    pips = dice.roll_1d6()
    hp_index = (hp - 1) * 6
    background_index = (hp_index + pips) - 1
    starting_item = maus_table.background[background_index]
    itema = maus_table.itema[background_index]
    itemb = maus_table.itemb[background_index]
    print("\tPips: "+str(pips)+"\t\tItem: "+itema+"\tItem: "+itemb)
    

def roll_henchman(is_pc=False):
    strength, dex, wil, hp = get_stats(is_pc)
    name = get_mausname()
    birthsign, disposition, coat, pattern, physical_detail = get_details()
    print("Maus: "+name)
    print("\tStrength: "+str(strength)+" \tDEX: "+str(dex)+" \tWIL: "+str(wil)+" \tHP: "+str(hp))
    print("\tBirthsign: "+birthsign+"\tDisposition: "+disposition)
    print("\tCoat: "+coat+"\tPattern: "+pattern+"\t\tDetail: "+physical_detail)
    return hp


def roll_henchmen():
    print("How many henchmen are we rolling?")
    val = utils.get_input_int()
    for index in range(val):
        roll_henchman()
        print("-")

def roll_npcs():
    print("How many NPCs are we rolling?")
    val = utils.get_input_int()
    for index in range(val):
        roll_npc()
        print("-")

def roll_npc():
    name = get_mausname()
    birthsign, disposition, coat, pattern, physical_detail = get_details()
    status, appearance, quirk, wants, relationship = get_npc_appearance()
    print("Maus: "+name+"\t\tSocial Status: "+status)
    print("\tBirthsign: "+birthsign+"\tDisposition: "+disposition)
    print("\tAppearance: "+appearance+"\tQuirk: "+quirk+"\tWants: "+wants)
    npc_status = ["Poor","Common","Common","Burghermouse","Guildmouse","Noblemaus"]
    if status == "Poor":
        cost = dice.roll_1d6()
    elif status == "Common":
        cost = dice.roll_1d6() * 10
    elif status == "Burghermouse":
        cost = dice.roll_1d6() * 50
    elif status == "Guildmouse":
        cost = dice.roll_1d4() * 100
    elif status == "Noblemaus":
        cost = dice.roll_1d4() * 1000
    print("\tCost: ["+str(cost)+"]")

def menu():
    func_list = [roll_henchmen,roll_main_character,roll_npcs]
    desc_list = ["Create Henchmen","Create Player Character","Create Villagers/NPCs"]
    utils.menu(func_list,desc_list,"Maus Creator",False)
