MEMORY = [t for t in map(int, input().split(','))]
MEMORY[1] = 12
MEMORY[2] = 2
i = 0
#print(len(MEMORY))
while MEMORY[i] != 99:
    if MEMORY[i] == 1:
        MEMORY[MEMORY[i+3]] = MEMORY[MEMORY[i+2]] + MEMORY[MEMORY[i+1]]
    elif MEMORY[i] == 2:
        MEMORY[MEMORY[i+3]] = MEMORY[MEMORY[i+2]] * MEMORY[MEMORY[i+1]]
    else:
        print("WRONG!")
        break
    #print(MEMORY)
    i += 4
print(MEMORY[0])
