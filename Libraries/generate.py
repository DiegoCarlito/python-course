# Python has a built-in module that you can use to make random numbers
import random
# from random import choice

# coin = random.choice(["heads", "tails"])
# number = random.randint(1, 10)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)