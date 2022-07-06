# chance_tables.py

# Stocking Adventure Site Room
room_type = ["empty", "empty", "Obstacle", "Trap", "Puzzle", "Lair"]
creature_present = [
    [True, True, True, False, False, False],
    [True, True, True, False, False, False],
    [True, True, False, False, False, False],
    [True, False, False, False, False, False],
    [True, True, True, False, False, False],
    [True, True, True, True, True, False]
]
treasure_present = [
    [True, False, False, False, False, False],
    [True, False, False, False, False, False],
    [True, False, False, False, False, False],
    [True, True, False, False, False, False],
    [True, True, True, True, True, False],
    [True, True, True, True, False, False]
]
empty_feature = [
    "Abandoned Insect Nest", "Cluster of Mushrooms", "Collapsed Wall or Ceiling", "Dried Bug shells", "Furniture made of garbage", 
    "Huge drawing of bat face", "Mess of tables and chairs", "Newspaper Clipping wallpaper", "Overgrown with moss", "Faded painted mural",
    "Platforms hanging over rapidly flowing water", "Roots bursting out of walls/floor/ceiling", "Rotting Pile of acorns", 
    "Scattered animal teeth", "Shiny candy-wrapper banners", "Snake Skull Doorway", "Steady dripping water", "Stern statue of ancient maus",
    "Uneven and cracked floor", "White quartz altar"
]
obstacle_feature = [
    "Locked door. Key can be found in another room. Knocking the door down takes time and makes noise.",
    "Steep climb. Without special equipment, mice risk exhaustion or falling.",
    "Room with an exit in the centre of the roof, 6 inches away from any wall.",
    "Device that creates an high-pitched scream. Each Turn spent here or in adjacent rooms gives Frightened Condition.",
    "Caved-in section of tunnel, leaving a gap too small to crawl through.",
    "Tunnel completely filled with water.",
    "Wide, deep puddle of mud blocking the way. Gives an Exhausted Condition per 6 inches traveled.",
    "Long, smooth, upwards sloping metal or plastic tube."
]
trap_feature = [
    "Large stone door, chiseled loose from frame. Device behind the door tips it forward when handle is turned.",
    "Long hallway flooded with water, electrified by large battery in an alcove.",
    "Dark room filled with noxious, explosive gas. Distinct smell of rotten eggs. d20 damage if ignited.",
    "Thin thread stretched across deadly fall. Safe if traveling slowly, one at a time.",
    "Pit blocking the way. A snake is asleep at the bottom.",
    "Door with three handles in the shape of mushrooms, one safe, the others poison. Poison handles deal d12 magical damage.",
    "Circle of enchanted mushrooms, with a young mouse inside. Those within try desperately to get others to enter.",
    "Floor is covered in sticky glue. Requires a STR save to break a foot loose."
]
puzzle_feature = [
    "",
    "",
    "",
    "",
    "",
    ""
]
lair_feature = [
    "",
    "",
    "",
    "",
    "",
    ""
]
treasure_type= [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
]
trinket = [
    "",
    "",
    "",
    "",
    "",
    ""
]
valuable = [
    "",
    "",
    "",
    "",
    "",
    ""
]
unusual = [
    "",
    "",
    "",
    "",
    "",
    ""
]
large = [
    "",
    "",
    "",
    "",
    "",
    ""
]
useful = [
    "",
    "",
    "",
    "",
    "",
    ""
]
magic_sword_class = ["Medium","Medium","Medium","Light","Heavy"]
magic_sword_types = ["Wrought Iron", "Intricate Fae Design", "Rusty Nail", "Snake Fang", "Toy Soldier's Sabre", "Water-Worn Glass", "Wolf Tooth", 
        "Silver Sewing Needle", "Thorny Rose Stem", "Congealed Shadow"]
magic_sword_cursed = [True, False, False, False, False, False]
cursed_sword_detail = [
    "Roll Damage Saves with Disadvantage; Lifted by Making a selfless sacrifice in a life-or-death situation",
    "",
    "",
    "",
    "",
    ""
]

island_table = ["N/A", "1 large continent", "1 large + 1 small island", "1 large + 2 small islands", "2 medium islands", "3 medium islands", "4 small islands"]
geo_table = ["N/A", "N/A", "Savanna",  "Wetlands", "Hills", "Lake", "River", "Forest", "Mountains", "Desert", "Jungle", "Canyon", "Volcano"]
race_table = ["N/A", "N/A", "Demonkind", "Seafolk", "Smallfolk", "Reptilian", "Dwarves", "Humans", "Elves", "Greenskins", "Animalfolk", "Giantkind", "Player’s choice"]
number_of_gods = [0, 1, 2, 2, 3, 3, 4]
god_domain_table = [ "N/A", "A Geography", "Something in Nature", "A Craft or Art", "An Endeavor", "Something around the home", "Something Grim"]
god_symbol_table = ["N/A", "Weapon", "Tool", "Animal", "Plant", "Natural", "Body Part"]
god_name_table = [
    ["N/A", "Amron", "Algalor","Emmalon","Goran","Aldiren","Inwegili"],
    ["N/A", "Amron", "Borumaht", "Mitholye", "Areris", "Zylis", "Shiro"],
    ["N/A","Algalor", "Penlathin", "Hesha", "Erelus", "Zaghora", "Abaal"],
    ["N/A", "Emmalon", "Ened", "Eldaren", "Baalas", "Ziri", "Delinas"],
    ["N/A", "Goran", "Pegenali", "Amariel", "Ontinti", "Ukraak", "Mablegon"],
    ["N/A", "Aldiren", "Vildir", "Therron", "Karne", "D’woinan", "Thingolfind"],
    ["N/A", "Inwegili", "Altas", "Findinus", "Sige", "Narnov", "Urnoste"]
]
settlement_table = ["N/A", "Farming Village", "Mining Settlement", "Resource Town", "Trade Post / Market Hub", "Frontier / Military Fort", "Monastery / Temple"]
hostiles_table = ["N/A", "Insect Hive", "Hostile Tribe", "Minor Faction", "Necromancer / Mad Mage", "Demon Lair", "Legendary Monster"]
