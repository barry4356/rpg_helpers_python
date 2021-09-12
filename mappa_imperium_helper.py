#!/usr/bin/python

#import sys
#import os
#import time
import random
#import pandas as pd
#from datetime import date
#from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import TimeoutException

#============= Chance Tables =============

island_table = ["N/A", "1 large continent", "1 large + 1 small island", "1 large + 2 small islands", "2 medium islands", "3 medium islands", "4 small islands"]
geo_table = ["N/A", "N/A", "Savanna",  "Wetlands", "Hills", "Lake", "River", "Forest", "Mountains", "Desert", "Jungle", "Canyon", "Volcano"]
race_table = ["N/A", "N/A", "Demonkind", "Seafolk", "Smallfolk", "Reptilian", "Dwarves", "Humans", "Elves", "Greenskins", "Animalfolk", "Giantkind", "Player’s choice"]
number_of_gods = [0, 1, 2, 2, 3, 3, 4]
god_domain_table = [ "N/A", "A Geography", "Something in Nature", "A Craft or Art", "An Endeavor", "Something around the home", "Something Grim"]
god_symbol_table = ["N/A", "Weapon", "Tool", "Animal", "Plant", "Natural", "Body Part"]
settlement_table = ["N/A", "Farming Village", "Mining Settlement", "Resource Town", "Trade Post / Market Hub", "Frontier / Military Fort", "Monastery / Temple"]
hostiles_table = ["N/A", "Insect Hive", "Hostile Tribe", "Minor Faction", "Necromancer / Mad Mage", "Demon Lair", "Legendary Monster"]

#============= UTILS =============
#def wait_by_id(id, driver):
#    delay = 10 # seconds for timeout
#    try:
#        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, id)))
#        #print ("Page is ready!")
#    except TimeoutException:
#        print ("Loading took too much time for ID: ", id, "!")
#
#def print_usage():
#    print ("\nUSAGE: ", os.path.basename(__file__), " [weekly/monthly] credentials_file\n")
#    
#def cash_to_float(cash):
#    my_val = cash.replace('$','')
#    my_val = my_val.replace(',','')
#    my_val = my_val.replace(' ','')
#    my_float = float(my_val)
#    return my_float

#=======================================
    
#============= GEN REPORTS =============
#def gen_weekly_report(cred_file):
#    print ("GENERATING WEEKLY REPORT...")
#    
#    print ("\nPulling Credentials...")
#    cred_df = pd.read_csv(cred_file)
#    accounts_df = pd.DataFrame(columns=['Date', 'Name', 'Value'])
#    debts_df = pd.DataFrame(columns=['Date', 'Name', 'Value'])
#    driver = webdriver.Chrome()
#    achieva_creds = cred_df.iloc[0]
#    pnc_creds = cred_df.iloc[1]
#    boa_creds = cred_df.iloc[2]
#    cone_creds = cred_df.iloc[3]
#    
#    print("\nLogging into PNC...")
#    pnc_login(pnc_creds[0], pnc_creds[1], driver)
#    
#    print("\nPulling Data From PNC...")
#    accounts_df, debts_df = pnc_get_accounts(accounts_df, debts_df, driver)
#    
#    print("\nLogging into Bank of America")
#    boa_login(boa_creds[0], boa_creds[1], driver)
#    
#    print("\nPulling Data From Bank of America...")
#    accounts_df, debts_df = boa_get_accounts(accounts_df, debts_df, driver)
#    
#    print("\nLogging into Achieva...")
#    achieva_login(achieva_creds[0], achieva_creds[1], driver)
#    
#    print("\nPulling Data From Achieva...")
#    accounts_df, debts_df = achieva_get_accounts(accounts_df, debts_df, driver)
#    
#    driver.close()
#    
#    #print("\nLogging into Capital One...")
#    print("\nPulling Data From Capital One...")
#    accounts_df, debts_df = cone_get_accounts(accounts_df, debts_df, driver)
#    
#    
#    print("\n")
#    print(accounts_df)
#    
#    print("\n")
#    print(debts_df)
#    
#    create_weekly_csv(accounts_df,"accounts.csv")
#    create_weekly_csv(debts_df,"debts.csv")
#        
#def gen_monthly_report():
#    print ("MONTHLY REPORT: UNDER CONSTRUCTION")
#    
#def create_weekly_csv(data_df,filename):
#    if not os.path.exists('Data'):
#        os.makedirs('Data')
#    if not os.path.exists('Data\Weekly'):
#       os.makedirs('Data\Weekly')
#       
#    if not os.path.isfile("Data\Weekly\\"+filename):
#        myfile = open("Data\Weekly\\"+filename, "w")
#        myfile.write("Date,Name,Value\n")
#        myfile.close()
#    
#    data_df.to_csv("Data\Weekly\\"+filename, mode='a', index=False, header=False)
    
#=========================================

#============= HANDLE LOGINS =============
#def achieva_login(username, password, driver):
#    driver.get("https://www.achievacu.com")
#    wait_by_id("loginDropDown", driver)
#    
#    driver.maximize_window()
#
#    wait_by_id("fnameIndex",driver)
#    driver.find_element_by_id("fnameIndex").send_keys(username)
#    driver.find_element_by_id("passwordIndex").send_keys(password)
#    driver.find_element_by_id("fnameIndex").submit()
#    return driver
#
#def pnc_login(username, password, driver):
#    driver.get("https://www.pnc.com/en/personal-banking/banking/online-and-mobile-banking/online-banking.html")
#    #time.sleep(3)
#    wait_by_id("container",driver)
#    driver.find_element_by_xpath("//*[@id=\"container\"]/div[2]/div/section/div/div/div/div[2]/div[2]/div[1]/div/div[2]/span/a").click()
#    time.sleep(2)
#    driver.find_element_by_name("userIdInput").find_element_by_name("userId").click()
#    driver.find_element_by_name("userIdInput").find_element_by_name("userId").send_keys(username)
#    driver.find_element_by_name("password").find_element_by_name("password").send_keys(password)
#    driver.find_element_by_name("password").find_element_by_name("password").submit()
#    time.sleep(5)
#    return driver
#    
#def boa_login(username, password, driver):
#    driver.get("https://secure.bankofamerica.com/login/sign-in/signOnV2Screen.go")
#    #time.sleep(3)
#    wait_by_id("enterID-input", driver)
#    driver.find_element_by_id("enterID-input").send_keys(username)
#    driver.find_element_by_id("tlpvt-passcode-input").send_keys(password)
#    driver.find_element_by_id("enterID-input").submit()
#    return driver
#    
#=====================================

#============= PULL DATA =============
#def achieva_get_accounts(accounts_df, debts_df, driver):
#    wait_by_id("module_accounts", driver)
#    the_date = date.today()
#    checking_value = cash_to_float(driver.find_element_by_xpath("//*[@id=\"account_65f6dc4c-9e03-4b10-9cba-93b6a6b94e2c\"]/a/div[2]/span[2]").text)
#    savings_value = cash_to_float(driver.find_element_by_xpath("//*[@id=\"account_9cb9c3ec-a68b-4c61-8f5b-15355ea6da00\"]/a/div[2]/span[2]").text)
#    credit_value = cash_to_float(driver.find_element_by_xpath("//*[@id=\"account_5ee3a21f-99fe-4b08-b520-034b7284e464\"]/a/div[2]/span[2]").text)
#    print("checking: ", checking_value, "; savings: ", savings_value)
#    accounts_df.loc[len(accounts_df.index)] = [the_date, "Achieva Checking", checking_value]
#    accounts_df.loc[len(accounts_df.index)] = [the_date, "Achieva Savings", savings_value]
#    debts_df.loc[len(debts_df.index)] = [the_date, "Achieva Credit", credit_value]
#    return accounts_df, debts_df
    
#def pnc_get_accounts(accounts_df, debts_df, driver):
#    the_date = date.today()
#    frame = driver.find_element_by_xpath('//frame[@name="center"]')
#    driver.switch_to.frame(frame)
#    table = driver.find_element_by_id("contentArea").find_element_by_id("leftCol_twoThirds").find_element_by_id("vwAccountsWrapper").find_elements_by_xpath("//table/tbody/tr")
#    checking_row = table[2].text
#    checking_split = checking_row.split('$')
#    checking_value = cash_to_float(checking_split[2].split('\n')[0])
#    credit_value = cash_to_float(checking_split[7])
#    print("checking: ", checking_value, "; credit: ", credit_value)
#    accounts_df.loc[len(accounts_df.index)] = [the_date, "PNC Checking", checking_value]
#    debts_df.loc[len(debts_df.index)] = [the_date, "PNC Credit", credit_value]
#    return accounts_df, debts_df
    
#def boa_get_accounts(accounts_df, debts_df, driver):
#    the_date = date.today()
#    wait_by_id("widget", driver)
#    checking_value = cash_to_float(driver.find_element_by_xpath("//*[@id=\"Traditional\"]/li[1]/div[1]/div[1]/span").text)
#    print("checking: ", checking_value)
#    accounts_df.loc[len(accounts_df.index)] = [the_date, "BOA Checking", checking_value]
#    return accounts_df, debts_df
#    
#def cone_get_accounts(accounts_df, debts_df, driver):
#    the_date = date.today()
#    data_valid = False
#    print("WIP: log into capital one and get the credit value...")
#    while data_valid != True:
#        data_valid = True
#        try:
#            val = float(input("Enter Value:"))
#        except ValueError:
#            data_valid = False
#            print("WRONG! Needs to be a valid number (no symbols)")
#    debts_df.loc[len(debts_df.index)] = [the_date, "Capital One Credit", val]
#    return accounts_df, debts_df
#            
#================================

def roll_1d6():
    return (random.randrange(6) + 1)
    
def roll_2d6():
    val = roll_1d6() + roll_1d6()
    return (val)
    
def roll_3d6():
    val = roll_1d6() + roll_1d6() + roll_1d6()
    return (val)

def turn_11():
    print("Mountains rise, forests grow. Small settlements begin to form, including an empire for each player to develop throughout the course of the game.");
    print("During this stage of the game, each player will take turns drawing out the islands, geography, factions, and resources in their 'Home Region'")

def turn_menu():
    exit = False;
    while exit != True:
        print("Please input either a turn number, or menu selection...")
        print("1.1: Island Creation")
        print("1.2: Geography")
        print("1.3: Resources")
        print("1.4: Major Faction")
        print("2.1: Number of Gods")
        print("2.2: Domains")
        print("2.3: Symbol")
        print("2.4: Name")
        print("3.1: Early Settlers")
        print("3.2: Hostile Neighbors")
        print("4.1: Exploration Begins")
        print("4.2: Neighbor Expansion")
        print("5.1: Worldwide Expansion")
        print("5.2: Neighbor Expansion")
        print("6.1: Final Era")
        print("6.2: Neighbor Expansion")
        print("6.3: Finalizing")
        print("0 - Main Menu")
        val = float(input("Enter Selection:"))
        print("\n")
        if(val == 0):
            exit = True
        
def dice_menu():
    exit = False;
    while exit != True:
        print("How many dice to roll?")
        print("1 - 1 Die")
        print("2 - 2 Dice")
        print("3 - 3 Dice")
        print("0 - Main Menu")
        val = float(input("Enter Selection:"))
        print()
        if(val == 0):
            exit = True
        if(val == 1):
            print(roll_1d6())
        if(val == 2):
            print(roll_2d6())
        if(val == 3):
            print(roll_3d6())
        print()
            
#============= MAIN MENU =============
#if len(sys.argv) >= 3:
#    if sys.argv[1] == "weekly":
#        cred_file = sys.argv[2]
#        gen_weekly_report(cred_file)
#else:
#    print_usage()

print ("\n===== MAPPA IMPERIUM HELPER =====\n")
exit = False;
while exit != True:
    print("Menu Selection...")

    print("0 - Exit")
    print("1 - Take Turn")
    print("2 - Roll Dice")
    val = float(input("Enter Selection:"))
    print("\n")
    
    if(val == 0):
        print ("HERE")
        exit = True
    
    if (val == 1):
        print(turn_menu())
        
    if (val == 2):
        dice_menu()
    
#================================
