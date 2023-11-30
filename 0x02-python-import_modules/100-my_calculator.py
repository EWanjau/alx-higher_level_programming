#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    op = ['+', '-', '*', '/']
    count = len(sys.argv)
    if count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if (sys.argv[2] is op[0]):
        print("{:d} {:s} {:d} = {:d}".format(a, op[0], b, add(a, b)))
    elif (sys.argv[2] is op[1]):
        print("{:d} {:s} {:d} = {:d}".format(a, op[1], b, sub(a, b)))
    elif (sys.argv[2] is op[2]):
        print("{:d} {:s} {:d} = {:d}".format(a, op[2], b, mul(a, b)))
    elif (sys.argv[2] is op[3]):
        print("{:d} {:s} {:d} = {:d}".format(a, op[3], b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
