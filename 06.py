import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
row = input()
while row != '':
    row = row.split(')')
    if row[0] not in G:
        G.add_node(row[0])
    G.add_node(row[0])
    G.add_edge(row[1], row[0])
    row = input()
count = 0
for node in G.nodes:
    for t in G.successors(node):
        succ = [s for s in G.successors(t)]
        count += 1
        while succ != []:
            t = succ[0]
            succ = [s for s in G.successors(t)]
            count += 1
    #    node = succ[0]
    #    count += 1
print(count)
