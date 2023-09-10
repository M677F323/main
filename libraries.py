#Many of libraries are already written so we can import them using import
import random

""" choice1 = random.choice(['HEADS','TAILS'])
print(choice1) """
#print heads or tails
from random import choice
choice1 = random.choice(['HEADS','TAILS'])
print(choice1)

#print random numbers
choice2 =random.randint(1,10)
print(choice2)

#print random cards
choice3 = ["King","Queen","Jack"]
random.shuffle(choice3)
print(choice3)

#we can also write like this
for i in choice3:
    print(i)