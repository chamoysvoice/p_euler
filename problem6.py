def problem6(n):
    return sum(range(n+1))**2 - sum([x**2 for x in range(n+1)])

print problem6(100)
