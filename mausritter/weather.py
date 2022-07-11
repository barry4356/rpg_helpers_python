#weather.py
import travel_tables
import utils
import travel_tables
import dice

def summer_weather():
    roll_daily_weather("Summer")

def fall_weather():
    roll_daily_weather("Fall")

def winter_weather():
    roll_daily_weather("Winter")

def spring_weather():
    roll_daily_weather("Spring")

def roll_daily_weather(season):
    if season == "Summer":
        print("Today's Weather: "+travel_tables.summer_weather[dice.roll_2d6()-2])

def daily_weather_menu():
    func_list = [summer_weather,fall_weather,winter_weather,spring_weather]
    desc_list = ["Roll Summer Weather","Roll Fall Weather",
        "Roll Winter Weather","Roll Spring Weather"]
    utils.menu(func_list,desc_list,"Weather Menu",False)

def roll_seasonal_event():
    print("WIP")

def menu():
    func_list = [daily_weather_menu,roll_seasonal_event]
    desc_list = ["Check Today's Weather","Create Seasonal Event"]
    utils.menu(func_list,desc_list,"Weather Menu",False)
