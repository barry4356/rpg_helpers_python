#dice_test.py
import dice

#Convert array of values to percent, based on total sample size
def array_to_pcnt(input_array):
    sample_size = 0
    for i in input_array:
        sample_size = sample_size + i
    return ([int(x / sample_size * 100) for x in input_array])

def test_custom_dice(sample_size = 100000):
    for custom_size in (6, 8, 10, 12, 20):
        results = [0] * (custom_size+2)
        for index in range(sample_size):
            roll_num = dice.roll_custom(custom_size)
            results[roll_num] = results[roll_num]+1
        results = array_to_pcnt(results)
        print ("Dice Size: ["+str(custom_size)+"]\t"+str(results))
    
def test_2d6(sample_size = 100000):
    results = [0] * (12+2)
    for index in range (sample_size):
        roll_num = dice.roll_2d6()
        results[roll_num] = results[roll_num]+1
    results = array_to_pcnt(results)
    print (results)

def roll_on_table_test(sample_size = 100000):
    for custom_size in (6, 8, 10, 12, 15, 20):
        results = [0] * (custom_size)
        test_table = [0] * (custom_size)
        for index in range(len(test_table)):
            test_table[index] = index
        for index in range(sample_size):
            roll = dice.roll_on_table(test_table)
            results[roll] = results[roll]+1
        results = array_to_pcnt(results)
        print ("Table Size: ["+str(custom_size)+"] \t"+str(results))

def test_d8_vs_2d6(sample_size = 100000):
    results_d8 = [0] * (10)
    results_d6 = [0] * (10)
    for index in range(sample_size):
        d6_roll = dice.roll_1d6()
        d6_rollb = dice.roll_1d6()
        if d6_rollb > d6_roll:
            d6_roll = d6_rollb
        d8_roll = dice.roll_1d8()
        results_d6[d6_roll] = results_d6[d6_roll]+1
        results_d8[d8_roll] = results_d8[d8_roll]+1
    results_d6 = array_to_pcnt(results_d6)
    results_d8 = array_to_pcnt(results_d8)
    d6_sum = results_d6[1] + 2 * results_d6[2] + 3 * results_d6[3] + 4 * results_d6[4] + 5 * results_d6[5] + 6 * results_d6[6]
    d8_sum = results_d8[1] + 2 * results_d8[2] + 3 * results_d8[3] + 4 * results_d8[4] + 5 * results_d8[5] + 6 * results_d8[6] + 7 * results_d8[7] + 8 * results_d8[8]
    print ("Dice (2-1)D6: \t"+str(results_d6)+"\tSum: "+str(d6_sum))
    print ("Dice D8: \t"+str(results_d8)+"\tSum: "+str(d8_sum))

print("Custom Dice Test")
test_custom_dice()
print()
print("2D6 Test")
test_2d6()
print()
print("Roll on Table Test")
roll_on_table_test()
print()
print("1D8 vs (2-1)D6")
test_d8_vs_2d6()
print()

