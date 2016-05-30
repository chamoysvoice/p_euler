# coding=utf-8
from __future__ import division
from math import sqrt

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(sv):
    return sv == sv[::-1]


def is_valid(n):
    return len(str(n)) == 3


def get_factors(n):
    for x in xrange(int(sqrt(n)), 0, -1):
        if n / x == int(n / x):
            return x, int(n / x)


def problem4():
    for x in xrange(999, 100, -1):
        temp_s = int(str(x)+str(x)[::-1])
        if is_palindrome(str(temp_s)):
            t, y = get_factors(temp_s)
            if is_valid(t) and is_valid(y):
                return temp_s

print problem4()

