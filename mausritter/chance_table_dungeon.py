# chance_tables.py

# Stocking Adventure Site Room
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
treasure_type= ["Magic Sword", "Random Spell", "Trinket", "Valuable Treasure", "Unusual Treasure", "Large Treasure",
    "Large Treasure", "Large Treasure", "Useful Treasure", "Useful Treasure", "d6x100 pips", "d6x50 pips", "d6x50 pips",
    "d6x50 pips", "d6x10 pips", "d6x10 pips", "d6x10 pips", "d6x5 pips", "d6x5 pips", "d6x5 pips"]
trinket = ["Ghost lantern (casts a light that banishes ghosts)", "Speaking shells (one speaks what the other hears)",
    "Breathing straw (tube that always contains air)", "Bat cultist’s dagger (grants passage into sanctum)",
    "Magic beans (grow fully in d6 Turns)", "Working human device (make up something fun)"]
valuable = ["Wheel of fine aged cheese (100p)", "Silver chain (2 slots, 500p)", "Jeweled pendant (400p)",
    "Gold ring (500p)", "Polished diamond (1000p)", "String of pearls (2 slots, 1500p)"]
unusual = ["Bundle of pungent herbs (200p to an apothecary)", "Odd-coloured dried mushrooms (200p to a witch)",
    "Eerily glowing stone (300p to a wizard)", "Heirloom of sentimental value to a noblemouse",
    "Legal documents granting land rights to the holder", "Treasure map"]
large = ["Oversized silver spoon (2 slots, 300p)", "Ivory comb (4 slots, 400p)",
    "Huge bottle of fine brandy (4 slots, 500p)", "Ancient mouse statue (4 slots, 500p)",
    "Ancient mouse throne (6 slots, 1000p)", "Giant golden wristwatch (4 slots, 1000p)"]
useful = ["d6 packs of rations, well preserved", "d6 bundles of torches", "Mundane weapon",
    "Mundane armour", "Mundane utility item", "Lost mouse, willing to help"]
magic_sword_class = ["Medium","Medium","Medium","Medium","Light","Heavy"]
magic_sword_types = ["Wrought Iron", "Intricate Fae Design", "Rusty Nail", "Snake Fang", "Toy Soldier's Sabre", "Water-Worn Glass", "Wolf Tooth", 
        "Silver Sewing Needle", "Thorny Rose Stem", "Congealed Shadow"]
magic_sword_cursed = [True, False, False, False, False, False]
cursed_sword_detail = [
    "Roll Damage Saves with Disadvantage; Lifted by Making a selfless sacrifice in a life-or-death situation",
    "When you gain an Exhausted Condition, gain another; Trading places with a poor farmer for a season",
    "Make a WIL save to not attack when threatened; Making lasting peace with a mortal enemy",
    "Reaction rolls are made with -1 modifier; Giving away everything you own, no cheating",
    "If you see an ally take damage, take a Frightened Condition; Fulfilling a mouse’s dying wish",
    "Spells cast in your presence always mark usage; Destroying an owl sorcerer’s source of power"
]