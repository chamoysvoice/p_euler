from __future__ import division

def multiplesOf20():
    i = 1
    while True:
        yield 2520 * i
        i+=1

def valid(n):
    for i in xrange(20, 1, -1):
        if n / i != int(n / i):
            return False
    return True

def problem5():
    return next(x for x in multiplesOf20() if valid(x))

print problem5()