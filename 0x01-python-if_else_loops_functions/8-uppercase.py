#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = ord(i)
        if(i >= 97 and i < 123):
            i = i - 32
        print(chr(i), end="")
    print()
