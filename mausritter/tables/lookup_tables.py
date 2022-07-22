#lookup_tables.py
import weather_tables
import treasure_tables

weather_table_name_list=[
    "Summer Weather","Fall Weather",
    "Winter Weather","Spring Weather",
    "Summer Event","Fall Event",
    "Winter Event","Spring Event"
]
weather_table_list=[
    weather_tables.summer_weather,weather_tables.fall_weather,
    weather_tables.winter_weather,weather_tables.spring_weather,
    weather_tables.summer_event, weather_tables.fall_event,
    weather_tables.winter_event,weather_tables.spring_event
]
magic_table_name_list=[
    "Magic Sword Classes","Magic Sword Types",
    "Cursed Sword Detail","Spell List"
]
magic_table_list=[
    treasure_tables.magic_sword_class,treasure_tables.magic_sword_types,
    treasure_tables.cursed_sword_detail,treasure_tables.spells
]
