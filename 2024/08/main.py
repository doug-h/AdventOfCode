import itertools

with open("input.txt") as file:
    grid = file.read().splitlines()
    W,H = len(grid[0]), len(grid)
    nodes = {complex(a,b): n for b,line in enumerate(grid) for a,n in enumerate(line) if n != '.'}
    antinodes1 = set()
    antinodes2 = set(nodes.keys())
    for types in set(nodes.values()):
        ns = (p for (p,n) in nodes.items() if n == types)
        for (p0,p1) in itertools.permutations(ns,2):
            d,a = p1-p0,p0
            while (a:=a-d).real in range(W) and a.imag in range(H):
                if(a == p0-d):
                    antinodes1.add(a)
                antinodes2.add(a)
    print(len(antinodes1))
    print(len(antinodes2))
