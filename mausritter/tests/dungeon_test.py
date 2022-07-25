#dungeon_test.py

import dungeon
import encounters
import treasure
import contracts

def test_dungeon(sample_size=10000):
    for i in range(sample_size):
        dungeon.create_dungeon_room()
        encounters.check_encounter()
        encounters.adventure_generator()
        treasure.roll_treasure()
        treasure.check_magic_sword()
        contracts.print_contract()
        dungeon.nwrm()
        dungeon.creature(argv=["faerie"])

    dungeon.nwrm(argv=["test`","test2"])
    dungeon.creature(argv=["frog"])
    dungeon.creature(argv=["mouse"])
    dungeon.creature(argv=["snake"])
    dungeon.creature(argv=["crow"])
    dungeon.creature(argv=["owl"])
    dungeon.creature(argv=["centipede"])
    dungeon.creature(argv=["rat"])

test_dungeon()