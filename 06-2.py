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

me = 'YOU'
santa = 'SAN'
santa_dict = dict()
me_dict = dict()
diff_set = set(santa_dict.keys()) & set(me_dict.keys())
i = 0
while len(diff_set) == 0:
    me = [t for t in G.successors(me)][0]
    me_dict[me] = i
    santa = [t for t in G.successors(santa)][0]
    santa_dict[santa] = i
    i += 1
    diff_set = set(santa_dict.keys()) & set(me_dict.keys())
joint = diff_set.pop()
print(santa_dict[joint] + me_dict[joint])
