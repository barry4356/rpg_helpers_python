import json

class hit():
    def __init__(self):
        self.data = self.gen_empty_data()

    def gen_empty_data(self):
        data = {}
        data['ap'] = 0
        data['poison'] = False
        return data
