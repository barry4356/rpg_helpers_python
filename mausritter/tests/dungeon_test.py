#dungeon_test.py

import dungeon
import encounters
import treasure
import contracts

def test_dungeon(sample_size=100000):
    for i in range(sample_size):
        dungeon.create_dungeon_room()
        encounters.check_encounter()
        encounters.adventure_generator()
        treasure.roll_treasure()
        treasure.check_magic_sword()
        contracts.print_contract()

test_dungeon()