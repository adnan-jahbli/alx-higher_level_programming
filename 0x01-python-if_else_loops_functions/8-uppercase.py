#!/usr/bin/python3
def uppercase(string):
    result = ""
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) & 223)
        else:
            result += char
    print(result)
