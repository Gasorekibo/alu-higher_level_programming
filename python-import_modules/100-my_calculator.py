#!/usr/bin/python3
from sys import argv
from calculator_1 import add, mul, div, sub
if __name__ == "__main__":
    num = len(argv)
    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == "+":
        res = add(a, b)
    elif op == "-":
        res = sub(a, b)
    elif op == "*":
        res = mul(a, b)
    elif op == "/":
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, op, b, res))
