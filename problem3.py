from __future__ import division
from math import sqrt
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


def problema3(n):
    return next(x for x in range(int(sqrt(n)), 0, -1) if n / x == int(n / x))

if __name__ == "__main__":
    print(problema3(600851475143))