#!/usr/bin/python3
def uppercase(string):
    for i in range(len(string)):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            number = 32
        else:
            number = 0
        print("{:c}".format(ord(string[i]) - number), end='')
    print()
