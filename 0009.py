import sys

a = [True] * 100000
for i in range(2, 100000):
    if (a[i - 1]):
        for j in range(i ** 2 - 1, 100000, i):
            a[j] = False
for s in sys.stdin:
    print(a[1:int(s)].count(True))
