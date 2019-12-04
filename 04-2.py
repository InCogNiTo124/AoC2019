import sys
start, end = tuple(map(int, input().split('-')))
from collections import Counter
def f(start, end):
    n = 0
    for k5 in range(start // 100000, end // 100000 + 1):
        for k4 in range(k5, 10):
            for k3 in range(k4, 10):
                for k2 in range(k3, 10):
                    for k1 in range(k2, 10):
                        for k0 in range(k1, 10):
                            g = ((((((k5*10) + k4)*10 + k3)*10) + k2)*10 + k1)*10 + k0
                            if g > end:
                                return n
                            c = Counter([k5, k4, k3, k2, k1, k0])
                            if any(t == 2 for t in c.values()):
                                n += 1
print(f(start, end))
