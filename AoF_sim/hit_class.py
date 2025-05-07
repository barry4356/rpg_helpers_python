import json

class hit():
    def __init__(self):
        self.attributes = self.gen_empty_attributes()
        self.ap = 0

    def gen_empty_attributes(self):
        data = {}
        data['poison'] = False
        return data
