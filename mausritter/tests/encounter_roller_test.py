#encounter_roller_test.py

import encounters
def test_encounter(sample_size=100000):
    for i in range(sample_size):
        encounters.roll_encounter()

test_encounter()