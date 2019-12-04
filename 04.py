import sys
start, end = tuple(map(int, input().split('-')))
def f(start, end):
    n = 0
    for k5 in range(start // 100000, end // 100000 + 1):
        for k4 in range(k5, 10):
            for k3 in range(k4, 10):
                for k2 in range(k3, 10):
                    for k1 in range(k2, 10):
                        for k0 in range(k1, 10):
                            g = ((((((k5*10) + k4)*10 + k3)*10) + k2)*10 + k1)*10 + k0
                            if len(set({k0, k1, k2, k3, k4, k5})) <= 5 and start <= g <= end:
                                n += 1
                            if g > end:
                                return n
print(f(start, end))
