import random

class Dice ():
    """Class describes game dice"""
    def __init__(self, side=6):
        self.side = side
    def RollDice(self):
        """Imitation of dice roll"""
        result = random.randint(1,self.side)
        print(f'Rolling the dice: {result}')

my_dice = Dice()
for i in range(10):
    my_dice.RollDice()
print()
my_dice.side = 10
for i in range(10):
    my_dice.RollDice()
print()
my_dice.side = 20
for i in range(10):
    my_dice.RollDice()
        