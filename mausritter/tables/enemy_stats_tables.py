#enemy_stats_tables.py
#HP,STR,DEX,WIL,Armor,Attack_Description,Desire_Description
#See page 22-24 of rulebook
cat_stats=[
    15,15,15,10,1,
    "d6 swipe, d8 bite.",
    "Wants to be served. If mice pledge fealty and give bribes, they may be allowed to live"
]
centipede_stats=[
    8,10,12,8,1,
    "d6 venemous bit (damages DEX instead of STR)\nCritical: Venom takes effect, d12 damage to STR",
    "Wants to wander and devour"
    ]

crow_stats=[
    12,12,15,15,1,
    "d8 peck\nFlies 3x normal speed, knows two songs",
    "Wants to protect the secret hallowed places from those that would do them harm"
    ]

frog_stats=[
    6,12,15,8,1,
    "d10 Spear or d6 tongue\nCritical: Leaps out of reach\nAlways goes first unless suprised, leaps 2x normal speed",
    "Wants to galantly complete their quest"
    ]

faerie_stats=[
    6,10,15,15,0,
    "d8 silver rapier\nKnows one spell",
    "Wants to further the Faerie Queen's strange agenda"
    ]

ghost_stats=[
    9,5,10,10,0,
    "ghostly power, d8 chilling touch (damages WIL)\nCritical damage: Possess the creature\nOnly harmed by silver or magic weapons",
    "Wants freedom from the pain that binds them to the mortal realm"
    ]

mouse_stats=[
    3,9,9,9,0,
    "d6 sword or d6 bow",
    "Wants to feel safe"
    ]

owl_stats=[
    15,15,15,15,1,
    "d10 bite\nFlies 3x normal speed. Knows two spells",
    "Wants to collect rare knowledge and spells"
    ]

snake_stats=[
    12,12,10,10,2,
    "d8 bite\nCritical damage: Swallow whole, d4 STR damage per Round until rescued or escape",
    "Wants to sleep undisturbed"
    ]

rat_stats=[
    3,12,8,8,0,
    "d6 cleaver",
    "Wants easy wealth, to take from the weak"
    ]

spider_stats=[
    6,8,15,10,1,
    "d6 poison bite (damages DEX instead of STR)\nCritical damage: Carry away in web",
    "Wants to feed its babies"
    ]

stats_lookup={
    "cat" : cat_stats,
    "centipede" : centipede_stats,
    "crow" : crow_stats,
    "frog" : frog_stats,
    "faerie" : faerie_stats,
    "ghost" : ghost_stats,
    "mouse" : mouse_stats,
    "owl" : owl_stats,
    "snake" : snake_stats,
    "rat" : rat_stats,
    "spider" : spider_stats
}