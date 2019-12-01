def f(x):
    fuel = 0
    while True:
        x = x // 3 - 2
        if x > 0:
            fuel += x
        else:
            break
    return fuel

fuel = sum(f(int(input())) for _ in range(100))
print(fuel)
