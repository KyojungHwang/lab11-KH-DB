# https://github.com/KyojungHwang/lab11-KH-DB
# Partner 1: KyoJung Hwang
# Partner 2: Dennis Bamaca Perez

import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a


def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid logarithm base.")
    if b <= 0:
        raise ValueError("Invalid logarithm argument.")
    return math.log(b, a)


def exp(a, b):
    return a ** b
