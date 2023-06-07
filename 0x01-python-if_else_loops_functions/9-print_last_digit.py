#!/usr/bin/python3
def print_last_digit(num):
    if num >= 0:
        LastDigit = num % 10
    else:
        LastDigit = num % -10
        LastDigit *= -1

    print("{:d}".format(LastDigit), end='')
    return (LastDigit)
