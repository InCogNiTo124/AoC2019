circuit = dict()

def insert(x, start_x, start_y, howmuch, direction):
    global circuit
    for _ in range(howmuch):
        start_x += direction[0]
        start_y += direction[1]
        #print("Inserting ({}, {})".format(start_x, start_y))
        if (start_x, start_y) not in circuit:
            circuit[(start_x, start_y)] = x
        elif circuit[(start_x, start_y)] != x:
            circuit[(start_x, start_y)] = 99
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
#print([abs(a) + abs(b)  for a, b, in circuit if circuit[a, b] == 99])
print(min([abs(a) + abs(b) for a, b in circuit if circuit[a, b] == 99]))

