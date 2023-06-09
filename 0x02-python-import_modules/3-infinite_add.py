#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    result = 0
    argv_len = len(sys.argv) - 1
    if argv_len >= 1:
        i = 1
        while i <= argv_len:
            result += int(argv[i])
            i += 1
    print(result)
