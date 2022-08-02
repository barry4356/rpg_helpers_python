#noble_test.py
import nobles
import fileops

def test_rolling_nobles(sample_size=1000):
    for index in range(sample_size):
        nobles.create_noble()
        filename = fileops.get_files(suffix="noble",path="mausritter/data/")
        if not filename:
            return
        filename = "mausritter/data/"+filename[0]
        noble_dict = fileops.deserialize_dict(filename)
        print(noble_dict["mission"])
        nobles.delete_noble(1)

print ("Testing rolling a Noble...")
test_rolling_nobles()