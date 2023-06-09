#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argv_len = len(argv) - 1
    if argv_len == 1:
        print("{} argument:".format(argv_len))
    elif argv_len > 1:
        print("{} arguments:".format(argv_len))
    else:
        print("{} arguments.".format(argv_len))

    i = 1
    while i <= argv_len:
        print("{}: {}".format(i, argv[i]))
        i += 1
