import networkx as nx

with open('2019/day_6_input.txt', 'r') as data:
    G = .Graph(item.strip().split(')') for item in data.readlines())

print(sum(nx.shortest_path_length(G, 'COM').values())) # Part 1

print(nx.shortest_path_length(G, 'YOU', 'SAN') - 2) # Part 2 
