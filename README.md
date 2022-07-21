# Python RPG Helpers
This is a set of python scripts meant to help run RPG games. Includes scripts for:
* Mappa Imperium
* Mausritter

## Mappa Imperium
Use [this link](https://nookrium.itch.io/mappa-imperium) to find the Mappa Imperium User manual. The scripts included in this repository include the chance tables, and perform dice rolls accordingly.

## Mausritter
Use [this link](https://mausritter.com/) to find the Mausritter user manual. The scripts included in this repository include chance tables from this manual, and
can perform many of the die rolls to generate characters, locations, quests, treasure, etc.

### Utility Layout
Below is an overview of the Mausritter Helper utilities:
```mermaid
flowchart LR
  A[Main Menu] --> B[Adventure Utils]
  A --> C[Combat Helper]
  A --> D[Maus Creator]
  A --> E[Weather Utils]
  A --> F[Hexmap Builder]
  A --> V[Hide Something]
  B --> G[Create New Room]
  B --> H[Roll for Encounter]
  B --> I[Create Encounter]
  B --> J[Random Adventure]
  B --> K[Roll Random Treasure]
  B --> L[Check sword for curse]
  B --> M[Check Wanted Poster]
  C --> N[Enemy Damage Tracker]
  C --> V[Roll New Creature]
  D --> O[Create Henchmen]
  D --> P[Create Player Character]
  D --> Q[Create Villagers/NPCs]
  E --> R[Check Today's Weather]
  E --> S[Create Seasonal Event]
  F --> T[Create New Hex]
  F --> U[Roll New Settlement]
  V --> W[Create New Faerie Hex]
```
