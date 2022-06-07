#!/usr/bin/python3

import sys
from calculator_1 import *
if __name__ == "__main__":
    op = ['+', '-', '*', '/']
    count = len(sys.argv)
    if count != 4:
        print("{:s}".format("Usage: ./100-my_calculator.py\
                <a> <operator> <b>"))
        exit(1)
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    if (sys.argv[2] is op[0]):
        print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
    elif(sys.argv[2] is op[1]):
        print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
    elif(sys.argv[2] is op[2]):
        print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
    elif(sys.argv[2] is op[3]):
        print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
