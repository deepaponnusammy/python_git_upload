"""
from random import *
answer = randint(0,10)
correct = False
while not(correct):
    guess = int(input("Guess a number (0-10): "))
    if guess < answer:
        print("Too low")
    elif guess > answer:
        print("Too high")
    else:
        print("Correct!")
        correct = True
"""
x=2            # create variable 'x'
print(x)       # print value     => 2
print(id(x))   # print id number => 1737348944
print(type(x)) # print type      => <class 'int'>
x=2             # integer
y=2.02          # float
z='3'           # string
print(str(x)+z) # 23
print(x+int(z)) # 5
a=[x,y,z]       # list
print(a[1])     # 2.02
b=(x,y)         # tuple
print(b[1])     # 2.02
c={'m':7,'n':8} # dictionary
print(c['m'])   # 7

import math
x=3.1415
print(math.sin(x)) # 9.265e-05

import numpy as np
x=np.pi
print(math.sin(x))  # 1.225e-16