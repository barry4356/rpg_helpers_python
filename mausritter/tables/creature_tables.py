#creature_tables.py
#HP,STR,DEX,WIL,Armor,Attack_Description,Desire_Description
#See page 22-24 of rulebook
enemy_stats = {
    "cat" : 
    [
        15,15,15,10,1,
        "d6 swipe, d8 bite.",
        "Wants to be served. If mice pledge fealty and give bribes, they may be allowed to live"
    ],
    "centipede" :
    [
        8,10,12,8,1,
        "d6 venemous bit (damages DEX instead of STR)\nCritical: Venom takes effect, d12 damage to STR",
        "Wants to wander and devour"
    ],
    "crow" :
    [
        12,12,15,15,1,
        "d8 peck\nFlies 3x normal speed, knows two songs",
        "Wants to protect the secret hallowed places from those that would do them harm"
    ],
    "frog" :
    [
        6,12,15,8,1,
        "d10 Spear or d6 tongue\nCritical: Leaps out of reach\nAlways goes first unless suprised, leaps 2x normal speed",
        "Wants to galantly complete their quest"
    ],
    "faerie" :
    [
        6,10,15,15,0,
        "d8 silver rapier\nKnows one spell",
        "Wants to further the Faerie Queen's strange agenda"
    ],
    "ghost" :
    [
        9,5,10,10,0,
        "ghostly power, d8 chilling touch (damages WIL)\nCritical damage: Possess the creature\nOnly harmed by silver or magic weapons",
        "Wants freedom from the pain that binds them to the mortal realm"
    ],
    "mouse" :
    [
        3,9,9,9,0,
        "d6 sword or d6 bow",
        "Wants to feel safe"
    ],
    "owl" :
    [
        15,15,15,15,1,
        "d10 bite\nFlies 3x normal speed. Knows two spells",
        "Wants to collect rare knowledge and spells"
    ],
    "snake" :
    [
        12,12,10,10,2,
        "d8 bite\nCritical damage: Swallow whole, d4 STR damage per Round until rescued or escape",
        "Wants to sleep undisturbed"
    ],
    "rat" :
    [
        3,12,8,8,0,
        "d6 cleaver",
        "Wants easy wealth, to take from the weak"
    ],
    "spider" :
    [
        6,8,15,10,1,
        "d6 poison bite (damages DEX instead of STR)\nCritical damage: Carry away in web",
        "Wants to feed its babies"
    ]
}

#See Table Page 21 of Rulebook
reactions = [
    "Hostile. How have the mice angered them?",
    "Unfriendly. How can they be appeased?",
    "Unfriendly. How can they be appeased?",
    "Unfriendly. How can they be appeased?",
    "Unsure. What could win them over?",
    "Unsure. What could win them over?",
    "Unsure. What could win them over?",
    "Talkative. What could they trade?",
    "Talkative. What could they trade?",
    "Talkative. What could they trade?",
    "Helpful. How can they help the mice?"
]

#See rulebook page 21
encounter_chances=["Encounter","Omen","None","None","None","None"]

#See rulebook page 22,23,24
creatures=["cat","centipede","crow","frog","faerie","ghost","mouse",
    "owl","snake","rat","spider"]
creature_details={
    "cat" :
    [
        ["Balthazar","Loves to eat the finest delicacies"],
        ["Melchior","Loves gold, jeweles, and wealth"],
        ["Solomon","Plays cruel games with captives"],
        ["Hammurabi","Rules with harsh, unbending logic"],
        ["Nefertiti","Loves art, poetry and beautiful things"],
        ["Zenobia","Formin an army of conquest, wants to rule"]
    ]
    ,
    "centipede" :
    [
        ["Giant","As big as a snake. 12hp, STR15, Armor2"],
        ["Swimming","Drags prey underwater"],
        ["Tiger","Yellow and black bands, d8 damage bite"],
        ["Glutton","Always hungry, never stops growing"],
        ["Racer","A delicacy, if you can catch them"],
        ["Feathered","Can glide short distances"]
    ]
    ,
    
    "crow" :
    [
        ["Dawn","Create a blindingly bright light"],
        ["Sorrow","All who hear: Make WIL save or take Frightened"],
        ["Sight","Vaguely foretell a future event"],
        ["Wind","Powerful gust. Make STR save or knocked down."],
        ["Past","See past event concerning those present"],
        ["Truth","All who hear: Cannot lie while the song lasts"]
    ]
    ,
    
    "frog" :
    [
        ["Gwal","Strong, kind of heart"],
        ["Phillip","Cursed human, searching for a cure"],
        ["Lurf","Unsound sense of honor, rash in anger"],
        ["Slup","Set on slaying a great beast, no matter the cost"],
        ["Uuu","Desperate to prove their strength at jousting"],
        ["Puc","Searching for the legendary Mug of Truth"]
    ]
    ,
    
    "faerie" :
    [
        ["Kidnapping","baby mice, to raise as their own"],
        ["Giving Gifts","that cause violent jealousy"],
        ["Playing Music","that bewitches mice into their service"],
        ["Using a Glamour","to appear as a mouse in distress"],
        ["Rotting","the food in winter storehouses"],
        ["Tricking","a settlement out of their legal standing"]
    ]
    ,
    
    "ghost" :
    [
        ["Shimmer","Create d3 illusions of itself"],
        ["Potergeist","Throws a creature/object d6 x 6inches"],
        ["Entrap","Pull a creature into the spirit realm for a Round"],
        ["Doom","Give Frightened Condition to a creature"],
        ["Rot","Destroys all rations carried by a creature"],
        ["Incorporeal","Float into wall/floor, reappear elsewhere"]
    ]
    ,
    
    "mouse" :
    [
        ["Thistle","Disgraced knight, still haughty"],
        ["Belladonna","Off-kilter wizard, looking for spells"],
        ["Hayseed","Trying to steal enough to buy back their farm"],
        ["Mandrake","Con artist. Appears unthreatening"],
        ["Marigold","Loves fire. Fears its absence"],
        ["Leif","Massive mouse exiled from far away land"]
    ]
    ,
    
    "owl" :
    [
        ["Bezalel","Builds mechanical servants"],
        ["Morgana","In league with a faerie kingdom"],
        ["Prospero","Creates chimeric servants"],
        ["Sparrowhawk","Can shape-shift into any other bird"],
        ["Crowley","Binds ghosts into spells"],
        ["Lechuza","Human witch trapped in owl form"]
    ]
    ,
    
    "snake" :
    [
        ["Wood","Carved stick of wood, ensorcelled into life"],
        ["Shadow","Slithers always just out of sight"],
        ["Bone","Snake skeleton, raised from the dead"],
        ["Eel","Lives underwater. Raises stolen snake eggs"],
        ["Scroll","Born with a spell etched into its scales"],
        ["Drake","Has wings, breathes small gouts of fame"]
    ]
    ,
    
    "rat" :
    [
        ["Dedratz","Construct elaborate scavenged traps"],
        ["Water Rats","Expert riverboat navigators"],
        ["Lab Rats","Bizarre looks, innate magical abilities"],
        ["Trashknights","1 armour tin breastplates and helms"],
        ["Gentlerats","Top hats and rumpled suits"],
        ["The Kings","Tails locked together in gordian knot"]
    ]
    ,
    
    "spider" :
    [
        ["Widow","Bright red markings, d10 damage bite"],
        ["Wolf","Furry, hunts in packs of d6 spiders"],
        ["Longlegs","Mostly peaceful, can walk on water"],
        ["Architect","Weave confusing tunnels of webs"],
        ["Blink","As an action, can teleport d6 x 10"],
        ["Ghost","Can only be harmed by silver or magic weapons"]
    ]
    
}
