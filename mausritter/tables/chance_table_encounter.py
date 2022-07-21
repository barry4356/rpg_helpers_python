# chance_tables.py
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
