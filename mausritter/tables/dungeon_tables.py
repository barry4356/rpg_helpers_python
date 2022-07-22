# dungeon_tables.py
# Stocking Adventure Site Room
# See Table Page 36 of Rulebook
room_type = ["Empty", "Empty", "Obstacle", "Trap", "Puzzle", "Lair"]
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
#See Table Page 37 of rulebook
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
    "Room with a floor made of an electrified copper plate. A piece of valuable treasure sits in the centre.",
    "Three feeding bottles with different-colored liquid inside. Each is inert individually but powerful/dangerous when mixed.",
    "A crystal, a magic sword embedded inside. The crystal is very hard, but will dissolve in stomach acid.",
    "Treasure is at the bottom of deep well.",
    "Large smooth steel bowl, upside down. Treasure taped to the inside ceiling of the bowl.",
    "Baited mousetrap. The lever is wired to a stone in the wall and will collapse the corridor if triggered"
]
lair_feature = ["Temporary encampment", "Recently taken from another creature", "Built by mice to hold the creature",
    "Protecting young", "Permanent home, newly settled", "Permanent home, comfortably appointed"]
