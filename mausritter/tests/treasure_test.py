#treasure_test.py

import treasure
def test_treasure(sample_size=100000):
    for i in range(sample_size):
        treasure.check_magic_sword()
        treasure.roll_treasure()

test_treasure()