import collections

def BK(R, P, X):
    if not P | X:
        yield R
    while(P):
        v = P.pop()
        yield from BK(R|set([v]), P & edges[v], X & edges[v])
        X.add(v)

with open("input.txt") as file:
    edges = collections.defaultdict(set)
    for s in file.readlines():
        a,b = s[0:2],s[3:5]
        edges[a].add(b)
        edges[b].add(a)


    largest_clique = set()
    max_size = 0
    for c in BK(set(), set(edges.keys()), set()):
        if len(c) > max_size:
            largest_clique = c
            max_size = len(c)
            for k in dict(edges):
                if len(edges[k]) <= max_size:
                    del edges[k]
            print(len(edges))

    print(','.join(sorted(largest_clique)))
