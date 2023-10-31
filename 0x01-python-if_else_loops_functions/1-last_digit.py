#!/usr/bin/python3
import random

N1 = random.randint(-10000, 10000)

N2 = N1*(-1) % 10 
print("Last digit of {} is {} ".format(N1, N2), end="")

if N2  > 5:
    print("and is greater than 5")

elif N2 == 0:
    print("and is 0")

else:
    print("and is less than 6 and not 0")
