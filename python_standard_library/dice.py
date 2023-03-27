from random import randint

"""It rolls a dice and prints a random number """

class Die:
    """A die that can be rolled"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides"""
        return randint(1, self.sides)

six_sides= Die()

#Rolling a 6-sided die 10 times"""

results = []
for roll_num in range(10):
    result = six_sides.roll_die()
    results.append(result)
print("Rolling a 6-sided die 10 times")
print(results)

ten_sides= Die(10)

#Rolling a 10-sided die 10 times"""

results = []
for roll_num in range(10):
    result = ten_sides.roll_die()
    results.append(result)
print("\nRolling a 10-sided die 10 times")
print(results)

twenty_sides= Die(20)

#Rolling a 6-sided die 10 times"""

results = []
for roll_num in range(10):
    result = twenty_sides.roll_die()
    results.append(result)
print("\nRolling a 20-sided die 10 times")
print(results)