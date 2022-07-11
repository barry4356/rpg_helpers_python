#weather.py
import weather_tables
import utils
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
        print("Today's Weather: "+weather_tables.summer_weather[dice.roll_2d6()-2])
    elif season == "Fall":
        print("Today's Weather: "+weather_tables.fall_weather[dice.roll_2d6()-2])
    elif season == "Winter":
        print("Today's Weather: "+weather_tables.winter_weather[dice.roll_2d6()-2])
    elif season == "Spring":
        print("Today's Weather: "+weather_tables.spring_weather[dice.roll_2d6()-2])

def daily_weather_menu():
    func_list = [summer_weather,fall_weather,winter_weather,spring_weather]
    desc_list = ["Roll Summer Weather","Roll Fall Weather",
        "Roll Winter Weather","Roll Spring Weather"]
    utils.menu(func_list,desc_list,"Weather Menu",False)

def seasonal_event_menu():
    func_list = [summer_event,fall_event,winter_event,spring_event]
    desc_list = ["Roll Summer Event","Roll Fall Event",
        "Roll Winter Event","Roll Spring Event"]
    utils.menu(func_list,desc_list,"Seasonal Event Menu",False)

def summer_event():
    roll_event("Summer")

def fall_event():
    roll_event("Fall")

def winter_event():
    roll_event("Winter")

def spring_event():
    roll_event("Spring")

def roll_event(season):
    if season == "Summer":
        print("Seasonal Event: "+dice.roll_on_table(weather_tables.summer_event))
    elif season == "Fall":
        print("Seasonal Event: "+dice.roll_on_table(weather_tables.fall_event))
    elif season == "Winter":
        print("Seasonal Event: "+dice.roll_on_table(weather_tables.winter_event))
    elif season == "Spring":
        print("Seasonal Event: "+dice.roll_on_table(weather_tables.spring_event))

def menu():
    func_list = [daily_weather_menu,seasonal_event_menu]
    desc_list = ["Check Today's Weather","Create Seasonal Event"]
    utils.menu(func_list,desc_list,"Weather Menu",False)
