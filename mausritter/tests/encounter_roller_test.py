#encounter_roller_test.py

import encounters
def test_encounter(sample_size=10000):
    for i in range(sample_size):
        encounters.roll_encounter()
        encounters.adventure_generator()
        encounters.check_encounter()
        encounters.roladv()
        encounters.enctr()
        encounters.enctr(argv=["-f"])

test_encounter()