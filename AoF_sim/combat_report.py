import json

# Class to contain data for a full report on a simulation's performance
class report():
    def __init__(self):
        self.results = []
        self.average_damage = 0
        self.max_damage = 0
        self.damage_odds = []

    def add_results(self, results):
        # Add results to internal list and re-calculate all compound data
        self.results.extend(results)
        totalDamage = 0
        for result in self.results:
            totalDamage += result.damage
            if result.damage > self.max_damage:
                self.max_damage = result.damage
        self.average_damage = totalDamage / len(self.results)
        self.calculate_damage_odds()

    # Take all damage results and calculate odds of each
    def calculate_damage_odds(self):
        odds = [0] * (self.max_damage+1)
        for value in self.results:
            odds[value.damage] = odds[value.damage] + 1
        for index, value in enumerate(odds):
            odds[index] = (value/len(self.results)) * 100
            if odds[index] < 1:
                odds[index] = round(odds[index],1)
            else:
                odds[index] = round(odds[index])
        self.damage_odds = odds
        
    # Print report to logger
    def print(self, logger):
        logger.info('\n=============')
        logger.info('Average damage: {0}'.format(self.average_damage))
        logger.info('======\nDamage Odds:')
        for damage in range(len(self.damage_odds)):
            logger.info(str(damage)+': '+ str(self.damage_odds[damage])+'%')
        logger.info('======')
        logger.info('=============\n')

# Class to contain a result from a single simulation
class result():
    def __init__(self):
        self.damage = 0