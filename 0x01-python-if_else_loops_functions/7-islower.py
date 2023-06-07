#!/usr/bin/python3
def islower(c):
    if c == "":
        c = ord(c) #this line was added just to generate error in this case
    LowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
    return c in LowercaseLetters
