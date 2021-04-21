from random import random

def weighted_random(weights):
    val = random()

    r = 0.0
    for i in range(0, len(weights)):
        r += weights[i]
        if r >= val:
            return i
