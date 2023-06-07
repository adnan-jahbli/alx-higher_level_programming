#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    LastDigit = number % 10
else:
    LastDigit = ((number * -1) % 10) * -1

print(f"Last digit of {number} is {LastDigit}", end=" ")
if LastDigit > 5:
    print("and is greater than 5")
elif LastDigit == 0:
    print("and is 0")
elif LastDigit < 6 and LastDigit != 0:
    print("and is less than 6 and not 0")
