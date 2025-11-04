# random
#import random
from random import *
# Generate random float number b/w 0-1
print(random())

# generate random float number b/w intervals
print(uniform(45.0, 89.2))

# generate random integer b/w intervals
print(randint(5,500))
print(randint(100000,999999))
# generate random integer b/w interval with step
print(randrange(2,100,2))

winner  = [1,2,3,4,5,6,7,8,9]
# fetch 1 random element from a sequence
print(choice(winner))

# fetch more than 1 random element from a sequence
print(choices(winner, k = 3))
print(sample(winner,3))

print(shuffle(winner))
print(winner)

seed(1)
print(randint(5,500))

seed(1520)
print(randint(5,500))
print(randrange(4,400,100))
seed(1)
print(randint(5,500))




