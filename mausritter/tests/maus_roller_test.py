#maus_roller_test.py

import maus_roller

def array_to_pcnt(input_array):
    sample_size = 0
    for i in input_array:
        sample_size = sample_size + i
    return ([int(x / sample_size * 100) for x in input_array])

def test_get_stats(sample_size=100000):
    results_str = [0] * (14)
    results_wil = [0] * (14)
    results_dex = [0] * (14)
    results_hp  = [0] * (14)
    for index in range (sample_size):
        strength, dex, wil, hp = maus_roller.get_stats(is_pc=False)
        results_str[strength] = results_str[strength]+1
        results_wil[wil] = results_wil[wil]+1
        results_dex[dex] = results_dex[dex]+1
        results_hp[hp] = results_hp[hp]+1
    print("NON-PLAYER-CHARACTER")
    print (array_to_pcnt(results_str))
    print (array_to_pcnt(results_wil))
    print (array_to_pcnt(results_dex))
    print (array_to_pcnt(results_hp))
    results_str = [0] * (14)
    results_wil = [0] * (14)
    results_dex = [0] * (14)
    results_hp  = [0] * (14)
    for index in range (sample_size):
        strength, dex, wil, hp = maus_roller.get_stats(is_pc=True)
        results_str[strength] = results_str[strength]+1
        results_wil[wil] = results_str[wil]+1
        results_dex[dex] = results_dex[dex]+1
        results_hp[hp] = results_hp[hp]+1
    print("PLAYER-CHARACTER")
    print (array_to_pcnt(results_str))
    print (array_to_pcnt(results_wil))
    print (array_to_pcnt(results_dex))
    print (array_to_pcnt(results_hp))

print("Test: get_stats")
test_get_stats()
print()
