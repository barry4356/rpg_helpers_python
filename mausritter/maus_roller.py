#maus_roller.py
#Use this to roll some Mice
import dice
import maus_table
import utils

def get_stats():
    str_dice = [0,0,0]
    str_dice[0] = dice.roll_1d6()
    str_dice[1] = dice.roll_1d6()
    str_dice[2] = dice.roll_1d6()
    str_dice.remove(min(str_dice))
    strength = sum(str_dice)
    dex_dice = [0,0,0]
    dex_dice[0] = dice.roll_1d6()
    dex_dice[1] = dice.roll_1d6()
    dex_dice[2] = dice.roll_1d6()
    dex_dice.remove(min(dex_dice))
    dex = sum(dex_dice)
    wil_dice = [0,0,0]
    wil_dice[0] = dice.roll_1d6()
    wil_dice[1] = dice.roll_1d6()
    wil_dice[2] = dice.roll_1d6()
    wil_dice.remove(min(wil_dice))
    wil = sum(wil_dice)
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

def roll_main_character():
    hp = roll_henchman()
    pips = dice.roll_1d6()
    hp_index = (hp - 1) * 6
    background_index = (hp_index + pips) - 1
    starting_item = maus_table.background[background_index]
    itema = maus_table.itema[background_index]
    itemb = maus_table.itemb[background_index]
    print("\tPips: "+str(pips)+"\t\tItem: "+itema+"\tItem: "+itemb)
    

def roll_henchman():
    strength, dex, wil, hp = get_stats()
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

def menu():
    func_list = [roll_henchmen,roll_main_character]
    desc_list = ["Create Henchmen","Create Player Character"]
    utils.menu(func_list,desc_list,"Maus Creator",False)
