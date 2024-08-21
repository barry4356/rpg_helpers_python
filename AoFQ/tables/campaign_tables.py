#campaign_tables.py

travel_event=[
        "Steep Mountain",
        "Mysterious Valley",
        "Raging River",
        "Dark Forest",
        "Bustling City",
        "Quiet Trail"
]

travel_event_desc=[
    "One random hero is Crippled.",
    "One random hero is Afflicted.",
    "One random hero is Impaired",
    "One random hero is Diseased",
    "One random hero gets 1 XP.",
    "Nothing happens."
]

primary_objectives=[
        "Clean Sweep",
        "Retrieval",
        "Area Search"
]

primary_objectives_legacy=[
        "Assassination",
        "Capture & Hold",
        "Seize Ground"
]

primary_objectives_desc={
   "Assassination" : "The sentries must have at least one villain, which gets Tou +3 and Qua +1, and counts as the AI goal. The objective is completed when the villain is killed",
   "Clean Sweep" : 'The centre of the table counts as the AI Goal. When the last model from the first wave of reinforcements is killed, it drops an objective marker within 1". Heroes may use a skill action whilst within 1" of the marker, and if they pass a Str test, the marker is removed and the objective is completed.',
   "Retrieval" : 'Place one objective marker within 6" of arandom table corner, which counts as the AIGoal (if the heroes are deployed in the samecorner, move the marker to the centre of thetable). Heroes within 1" of the marker maypick it up by using a skill action and passing a Dex test, and drop it within 1" if they areshaken. The objective is completed when thehero carrying the marker ends its activationwithin 6" of the hero deployment corner.',
   "Area Search" : 'Place three objective markers randomly atthe centre of three different table quarters orthe centre of the table, and the markerclosest to the hero nearest to an enemycounts as its AI Goal. Heroes may use a skillaction whilst within 1“ of a marker, and if they pass a Wil test, remove the marker androll one die. On a 5+, or if it was the lastmarker, the objective is completed.',
   "Capture & Hold" : "Place one objective marker randomly at the centre of a table quarter or the centre of the table, which counts as the AI goal. At the end of each round, if a hero is within 3\" of the marker whilst enemies aren't, then it's seized. The objective is completed once the heroes have seized the marker for D3+3 consecutive rounds.",
   "Seize Ground" : "Place one objective marker at the centre of each table quarter, and the closest marker is the AI goal. At the end of each round, if a hero is within 3\" of the marker whilst enemies aren't, then it’s seized, and remains seized as long as no enemies are within 3\" of the marker whilst heroes aren’t at the end of any other round. The objective is completed once the heroes are seizing D3+1 markers at the end of any round."
}

secondary_objectives=[
        "Interrogate",
        "Capture",
        "Escort",
        "Sabotage"
]

secondary_objectives_legacy=[
        "Ransack",
        "Dominate"
]

secondary_objectives_desc={
   "Interrogate" : 'The centre of the table counts as the AI Goal.When the last model from the next wave ofreinforcements is killed, it drops an objectivemarker within 1“. Heroes may use a skillaction whilst within 1“ of the marker, and ifthey pass a Wil test, the marker is removed and the objective is completed.',
   "Capture" : 'Place one objective marker at the centre of the table, which counts as the AI Goal. Heroes within 1“ of the marker may pick it up by using a skill action and passing a Str test, and drop it within 1“ if they are shaken. The objective is completed when the hero carrying the marker ends its activation within 6“ of any corner.',
   "Escort" : 'Place one objective marker within 3“ of one random hero, which counts as the AI Goal, and place one extraction marker within 6“ of the table corner furthest from that hero. Heroes within 1“ of the marker may pick it up by using a skill action and passing a Str test, and drop it within 1“ if they are shaken. When the hero carrying the objective ends its activation within 3“ of the extraction marker the objective is completed.',
   "Sabotage" : 'Place one objective marker within 6“ of the table corner furthest from one random hero, which counts as the AI Goal. Heroes may use a skill action whilst within 1“ of the marker, and if they pass a Wil test, the marker is removed and the objective is completed.',
   "Ransack" : 'Place one objective marker at the centre of the table, which becomes the AI goal. At the end of each round, if a hero is within 3" of the marker whilst enemies aren\'t, one hero within 3" of it may take a Dex test, and add a token to it if passed. The objective is completed once the marker has 2 tokens.',
   "Dominate" : 'Place one objective marker at the centre of each table quarter, which becomes the AI goal. At the end of each round, if a hero is within 1" of the marker whilst enemies aren’t, one hero within 3" of each may take a Wil test, and if passed the marker is removed. The objective is completed once two objectives have been removed.'
}



alertness=["Careless","Vigilant","Full Alert"]

injury=["Chest Wound","Blinded Eye","Smashed Leg","Broken Arm","Spinal Injury","Crushed Spirit"]
