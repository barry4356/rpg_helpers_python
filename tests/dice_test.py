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

print("Custom Dice Test")
test_custom_dice()
print()
print("2D6 Test")
test_2d6()
print()

