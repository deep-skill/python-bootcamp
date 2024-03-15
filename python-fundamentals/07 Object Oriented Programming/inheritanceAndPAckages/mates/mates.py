from math import factorial as fact


def factorial(n):
    return fact(n)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def to_square(n):
    return n ** 2

