# docs.python.org/3/library/random.html

# import random
from random import choice
coin = choice(["heads", "tails"]) # random.choice(["heads", "tails"])
print(coin)

from random import randint
number = randint(1, 10)
print(number)

from random import shuffle
deck = ["ace", "king", "queen", "jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
shuffle(deck)
for card in deck:
    print(card)
