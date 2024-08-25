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
        "Area Search",
        "Target Defense",
        "Investigation",
        "Delivery"
]

primary_objectives_legacy=[
        "Assassination",
        "Capture & Hold",
        "Seize Ground"
]

primary_objectives_narrative=[
        "Last Call",
        "Doors of Tsevadraz",
        "Bog Battle",
        "Trapped Among Tombs",
        "Silencing Sentries",
        "Heart of Darkness"
]

primary_objectives_desc={
   "Assassination" : "The sentries must have at least one villain, which gets Tou +3 and Qua +1, and counts as the AI goal. The objective is completed when the villain is killed",
   "Clean Sweep" : 'The centre of the table counts as the AI Goal. When the last model from the first wave of reinforcements is killed, it drops an objective marker within 1". Heroes may use a skill action whilst within 1" of the marker, and if they pass a Str test, the marker is removed and the objective is completed.',
   "Retrieval" : 'Place one objective marker within 6" of arandom table corner, which counts as the AIGoal (if the heroes are deployed in the samecorner, move the marker to the centre of thetable). Heroes within 1" of the marker maypick it up by using a skill action and passing a Dex test, and drop it within 1" if they areshaken. The objective is completed when thehero carrying the marker ends its activationwithin 6" of the hero deployment corner.',
   "Area Search" : 'Place three objective markers randomly atthe centre of three different table quarters orthe centre of the table, and the markerclosest to the hero nearest to an enemycounts as its AI Goal. Heroes may use a skillaction whilst within 1" of a marker, and if they pass a Wil test, remove the marker androll one die. On a 5+, or if it was the lastmarker, the objective is completed.',
   "Capture & Hold" : 'Place one objective marker randomly at the centre of a table quarter or the centre of the table, which counts as the AI goal. At the end of each round, if a hero is within 3" of the marker whilst enemies aren\'t, then it\'s seized. The objective is completed once the heroes have seized the marker for D3+3 consecutive rounds.',
   "Seize Ground" : 'Place one objective marker at the centre of each table quarter, and the closest marker is the AI goal. At the end of each round, if a hero is within 3" of the marker whilst enemies aren\'t, then it\'s seized, and remains seized as long as no enemies are within 3" of the marker whilst heroes aren\'t at the end of any other round. The objective is completed once the heroes are seizing D3+1 markers at the end of any round.',
   "Target Defense" : 'Place one objective marker randomly at the centre of a table quarter or the centre of the table, which counts as the AI Goal. Heroes may use a skill action whilst within 1" of the marker and take a Str test. If passed, at the end of each round, if a hero is within 3" of the marker while enemies aren\'t, then it\'s seized, and it gets one token. The objective is completed once the marker has 4*X tokens (where X is the chosen difficulty level).',
   "Investigation" : 'Place two objective markers randomly at the centre of two different table quarters or the centre of the table, and the marker closest to the hero nearest to an enemy counts as its AI Goal. Heroes may use a skill action whilst within 1" of a marker, and if they pass a Dex test, the marker is removed. The objective is completed once both markers are removed.',
   "Delivery" : 'Place two delivery markers within 6" of two different random table corners (if the heroes are deployed in the same corner as a marker, move it to the centre of the table). When the heroes deploy, place one objective marker in their deployment zone, which counts as the AI Goal. Heroes within 1" of the marker may pick it up by using a skill action and passing a Wil test, and drop it within 1" if they are shaken. When the hero carrying the objective ends its activation within 3" of a delivery marker, remove that marker. The objective is completed once both markers are removed.',
   "Last Call" : 'Heroes enter on one table edge. Place three hiding spot markers evenly spaced along the farthest table edge. Heroes may use a skill action whilst within 1" of a marker, and if they pass a Dex or Wil test, remove the marker and roll one die. On a 5+, or if it was the last marker, the heroes have found a hiding spot, and the objective is completed. All heroes must be within 3" of the hiding spot to end the round.',
   "Doors of Tsevadraz" : 'Place marker for gateway on far edge from heroes with 4*X tokens on it (where X is the difficulty level). This counts as the AI goal. Heroes may use a skill action within 1" of the marker and take a Str test to unlock the gate. If passed, at the end of the round if the hero is still within 3" of the marker, remove one token from it. Objective is complete when all tokens are removed. All heroes must be within 3" of marker to end the round.',
   "Bog Battle" : 'Heroes deploy within 6" of table\'s center. Center of the table counds as the AI goal. When the last model from the second wave of reinforcements is killed, it drops an objective marker. heroes may use a skill action within 1" of the marker and if they pass a Dex check, the marker is removed and the objective is complete.',
   "Trapped Among Tombs" : 'Heroes enter on table corner. Place 3 markers diagnolly evenly spaced across the board perpendicular to heroes\' entry corner. Markers count as AI goals, with priority being closest to heroes. Heroes may use skill action within 1" of a marker, and if the pass a Wil test, remove the marker and roll a die. On a 5+, or if it was the last marker, objective is complete.',
   "Silencing Sentries" : 'The heroes must be deployed within 6” of a random table corner. Place two sentry alarm markers within 6" of the table center, but 12" away from each other. The marker closest to the hero nearest to an enemy counts as its AI Goal. Heroes may use a skill action whilst within 1“ of a marker, and if they pass a Str test, the marker is removed. The objective is completed once both markers are removed. If an enemy unit that starts or ends its activation within 3” of a sentry alarm marker has line of sight to a hero, then players get +1 when rolling for alertness increase until the end of the mission. This rule is only activated once per alarm.',
   "Heart of Darkness" : 'Place nine objective markers in a grid at the center of the table, with 12" between each row/column. Then randomly remove one from each row. Heroes may use a skill action whilst within 1“ of a marker, and if they pass a Wil test, remove the marker and roll one die. On a 6+, or if it was the last marker, the heroes have found and completed the objective.'
}

secondary_objectives=[
        "Interrogate",
        "Capture",
        "Escort",
        "Sabotage",
        "Safeguard",
        "Scavenge"
]

secondary_objectives_legacy=[
        "Ransack",
        "Dominate"
]

secondary_objectives_narrative=[
        "Last Call",
        "Trapped Among Tombs"
]

secondary_objectives_desc={
   "Interrogate" : 'The centre of the table counts as the AI Goal. When the last model from the next wave of reinforcements is killed, it drops an objective marker within 1". Heroes may use a skill action whilst within 1" of the marker, and if they pass a Wil test, the marker is removed and the objective is completed.',
   "Capture" : 'Place one objective marker at the centre of the table, which counts as the AI Goal. Heroes within 1" of the marker may pick it up by using a skill action and passing a Str test, and drop it within 1" if they are shaken. The objective is completed when the hero carrying the marker ends its activation within 6" of any corner.',
   "Escort" : 'Place one objective marker within 3" of one random hero, which counts as the AI Goal, and place one extraction marker within 6" of the table corner furthest from that hero. Heroes within 1" of the marker may pick it up by using a skill action and passing a Str test, and drop it within 1" if they are shaken. When the hero carrying the objective ends its activation within 3" of the extraction marker the objective is completed.',
   "Sabotage" : 'Place one objective marker within 6" of the table corner furthest from one random hero, which counts as the AI Goal. Heroes may use a skill action whilst within 1" of the marker, and if they pass a Wil test, the marker is removed and the objective is completed.',
   "Ransack" : 'Place one objective marker at the centre of the table, which becomes the AI goal. At the end of each round, if a hero is within 3" of the marker whilst enemies aren\'t, one hero within 3" of it may take a Dex test, and add a token to it if passed. The objective is completed once the marker has 2 tokens.',
   "Dominate" : 'Place one objective marker at the centre of each table quarter, which becomes the AI goal. At the end of each round, if a hero is within 1" of the marker whilst enemies aren\'t, one hero within 3" of each may take a Wil test, and if passed the marker is removed. The objective is completed once two objectives have been removed.',
   "Sabotage" : 'Place one objective marker within 6" of the table corner furthest from one random hero, which counts as the AI Goal. Heroes may use a skill action whilst within 1" of the marker, and if they pass a Wil test, the marker is removed and the objective is completed.',
   "Safeguard" : 'Place one objective marker at the centre of the table, which counts as the AI Goal. Heroes may use a skill action whilst within 1" of the marker and take a Dex test. If passed, at the end of each round, if a hero is within 3" of the marker while enemies aren\'t, then it\'s seized, and it gets one token. The objective is completed once the marker has 2*X tokens (where X is the chosen difficulty level).',
   "Scavenge" : 'Place two objective markers within 6" of the two corners closest to one random hero, and the marker closest to the hero nearest to an enemy counts as its AI Goal. Heroes may use a skill action whilst within 1" of a marker, and if they pass a Dex test, remove the marker and roll one die. On a 4+, or if it was the last marker, the objective is completed.',
   "Last Call" : 'Place two markers on two random table edges, which count as AI Goals. Heroes may use a skill action whilst within 1" of the markers to remove both markers and the objective is completed. If the heroes complete the secondary objective, immediately deploy a new wave of reinforcements.',
   "Trapped Among Tombs" : 'Place one marker on furthest corner from heroes\' entry, which counts as an AI goal. Heroes suffer D3 stress whilst within 1" of the marker, removing the marker and completing the objective.'
}



alertness=["Careless","Vigilant","Full Alert"]

injury=["Chest Wound","Blinded Eye","Smashed Leg","Broken Arm","Spinal Injury","Crushed Spirit"]
