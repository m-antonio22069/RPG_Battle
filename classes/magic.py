import random


class Spell:
    def __init__(self, name, cost, dmg, tp):
        self.name=name
        self.cost = cost
        self.dmg = dmg
        self.tp = tp

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg+15
        return random.randrange(start=low, stop=high)
