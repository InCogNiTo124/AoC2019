from itertools import product
MEMORY_orig = [t for t in map(int, input().split(','))]
for n1, n2 in product(range(100), range(100)):
    MEMORY = MEMORY_orig.copy()
    assert MEMORY is not MEMORY_orig
    i = 0
    MEMORY[1] = n1
    MEMORY[2] = n2
    while MEMORY[i] != 99:
        if MEMORY[i] == 1:
            MEMORY[MEMORY[i+3]] = MEMORY[MEMORY[i+2]] + MEMORY[MEMORY[i+1]]
        elif MEMORY[i] == 2:
            MEMORY[MEMORY[i+3]] = MEMORY[MEMORY[i+2]] * MEMORY[MEMORY[i+1]]
        else:
            print("WRONG!")
            break
        i += 4
    if MEMORY[0] == 19690720:
        print(100*n1+n2)
        break

