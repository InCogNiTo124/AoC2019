circuit = {(0, 0): [0, 0]}

def insert(x, start_x, start_y, howmuch, direction):
    global circuit
    length = circuit[(start_x, start_y)][x]
    for _ in range(howmuch):
        length += 1
        start_x += direction[0]
        start_y += direction[1]
        t = circuit.get((start_x, start_y), [0, 0])
        t[x] = length
        circuit[(start_x, start_y)] = t
    return start_x, start_y


for i in range(2):
    wire_x, wire_y = 0, 0
    parts = input().split(',')
    #print(parts)
    for wirepart in parts:
        if wirepart[0] == "R":
            wire_x, wire_y = insert(i, wire_x, wire_y, int(wirepart[1:]), direction=(1, 0))
        elif wirepart[0] == "L":
            wire_x, wire_y = insert(i, wire_x, wire_y, int(wirepart[1:]), direction=(-1, 0))
        elif wirepart[0] == "U":
            wire_x, wire_y = insert(i, wire_x, wire_y, int(wirepart[1:]), direction=(0, 1))
        elif wirepart[0] == "D":
            wire_x, wire_y = insert(i, wire_x, wire_y, int(wirepart[1:]), direction=(0, -1))
print(min(a + b for a, b in circuit.values() if a > 0 and b > 0))
