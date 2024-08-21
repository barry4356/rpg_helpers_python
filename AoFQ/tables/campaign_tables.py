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
        "Assassination",
        "Clean Sweep",
        "Retrieval",
        "Search Area",
        "Capture & Hold",
        "Seize Ground"
]

primary_objectives_desc={
   "Assassination" : "The sentries must have at least one villain, which gets Tou +3 and Qua +1, and counts as the AI goal. The objective is completed when the villain is killed",
   "Clean Sweep" : "Whenever all enemies are killed, a wave of reinforcements is deployed at the end of the round. The centre of the table is the AI goal. The objective is completed after all sentires and the first wave of reinforcements has been killed.",
   "Retrieval" : "Whenever an enemy unit is destroyed, roll one die, on a 6 it drops an objective marker, which counts as the AI goal. Heroes may pick the marker up by using a skill action whilst within 1\", and drop it on the spot if they take any damage. The objective is completed once a hero carries the marker within 3\" of the furthest table corner from where the marker was dropped.",
   "Search Area" : "Place one objective marker at the centre of each table quarter, and one at the centre of the table, and the closest marker is the AI goal. At the end of each round, if a hero is within 3\" of a marker whilst enemies aren't, then the marker is removed. The objective is completed once D3+2 markers have been removed.",
   "Capture & Hold" : "Place one objective marker randomly at the centre of a table quarter or the centre of the table, which counts as the AI goal. At the end of each round, if a hero is within 3\" of the marker whilst enemies aren't, then it's seized. The objective is completed once the heroes have seized the marker for D3+3 consecutive rounds.",
   "Seize Ground" : "Place one objective marker at the centre of each table quarter, and the closest marker is the AI goal. At the end of each round, if a hero is within 3\" of the marker whilst enemies aren't, then it’s seized, and remains seized as long as no enemies are within 3\" of the marker whilst heroes aren’t at the end of any other round. The objective is completed once the heroes are seizing D3+1 markers at the end of any round."
}

secondary_objectives=[
        "Interrogate",
        "Capture",
        "Escort",
        "Sabotage",
        "Ransack",
        "Dominate"
]

secondary_objectives_desc={
   "Interrogate" : 'One random enemy unit from the reinforcements becomes the AI goal. When that unit is destroyed, replace it with a marker. Heroes within 1" may take a skill action, and if they pass a Wil test the objective is completed.',
   "Capture" : 'Place one objective marker within 6“ of the reinforcement table corner, which becomes the AI goal. At the end of each round, the marker moves 12" towards the opposite table corner, and if it moves within 3" of it, then it is removed from play. If no enemy unit is within 3" of the marker, heroes within 1" of it may take a skill action, and if they pass a Str test, then the marker is removed and the objective is completed.',
   "Escort" : 'Place one objective marker in the hero deployment zone, which becomes the AI goal. Heroes may pick up the marker by using a skill action and passing a Str test whilst within 1", and drop it on the spot if they take any damage. The objective is completed once a hero carries the marker within 3" of the opposite table corner in which the heroes deployed.',
   "Sabotage" : 'Place one objective marker within 6" of the reinforcement table corner, which becomes the AI goal. Heroes may use a skill action whilst within 1“ of a marker, and if they pass a Dex test the marker is removed and the objective is completed.',
   "Ransack" : 'Place one objective marker at the centre of the table, which becomes the AI goal. At the end of each round, if a hero is within 3" of the marker whilst enemies aren\'t, one hero within 3" of it may take a Dex test, and add a token to it if passed. The objective is completed once the marker has 2 tokens.',
   "Dominate" : 'Place one objective marker at the centre of each table quarter, which becomes the AI goal. At the end of each round, if a hero is within 1" of the marker whilst enemies aren’t, one hero within 3" of each may take a Wil test, and if passed the marker is removed. The objective is completed once two objectives have been removed.'
}



alertness=["Careless","Vigilant","Full Alert"]

injury=["Chest Wound","Blinded Eye","Smashed Leg","Broken Arm","Spinal Injury","Crushed Spirit"]
