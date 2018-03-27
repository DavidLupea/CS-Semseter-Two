#David Lupea
#IntroCS2 pd5
#HW 9 -- Controlled Randomness
#2018-02-28


import random                                                               #Imports the necesary library

flipCoin = lambda : "heads" if random.randint(1,2) == 1 else "tails"        #Picks a numbber(either one or two and if it is 1, it prints heads, otherwise it prints tails

def rollDie(n):
    return random.randint(1, n)                                             #Picks a random number between 1 and n inclusive and prints it
