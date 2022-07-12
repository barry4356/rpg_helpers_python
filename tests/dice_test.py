#dice_test.py
import dice

def test_custom_dice():
    for custom_size in (6, 8, 10, 12, 20):
        results = [0] * (custom_size+2)
        for index in range(1000):
            roll_num = dice.roll_custom(custom_size)
            results[roll_num] = results[roll_num]+1
        print ("Dice Size: ["+str(custom_size)+"]\t"+str(results))
    
def test_2d6():
    results = [0] * (12+2)
    for index in range (10000):
        roll_num = dice.roll_2d6()
        results[roll_num] = results[roll_num]+1
    print (results)

def roll_on_table_test():
    for custom_size in (6, 8, 10, 12, 15, 20):
        results = [0] * (custom_size)
        test_table = [0] * (custom_size)
        for index in range(len(test_table)):
            test_table[index] = index
        for index in range(1000):
            roll = dice.roll_on_table(test_table)
            results[roll] = results[roll]+1
        print ("Table Size: ["+str(custom_size)+"] \t"+str(results))

print("Custom Dice Test")
test_custom_dice()
print()
print("2D6 Test")
test_2d6()
print()
print("Roll on Table Test")
roll_on_table_test()
print()

