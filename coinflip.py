'''
COIN FLIPSS!!! YAY
'''
import random

try:
    x = int(input('How many times do you want to flip the coin? '))
    n = 0
    t = 0
    h = 0
    coinfliplist = []
    while n < x:
        decision = random.randint(1,2)
        if decision == 1:
            coinfliplist.append('Heads')
            h += 1
        else:
            coinfliplist.append('Tails')
            t += 1
        n += 1
    print(coinfliplist)
    print(f'Number of Tails: {t}')
    print(f'Number of Heads: {h}')

except ValueError:
    print("Why no thank you for not putting a number")