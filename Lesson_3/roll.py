import random

def roll(probability):
    return random.randint(0, 100) < probability

for i in range(20):
    print(roll(0.000000001))
