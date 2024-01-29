import collections
import itertools

data = [(l[:3], l[4:].split()) for l in open("data.txt")]

name_counts = collections.Counter()
for n, s in data:
    name_counts[n] += 1
    name_counts.update(s)
vertices = set(name_counts)

print(f"Edges: {name_counts.total()}, Vertices: {len(vertices)}")

edges = {v: set() for v in vertices}
for n, s in data:
    edges[n].update(s)
    for c in s:
        edges[c].add(n)

A = set(vertices)
B = set()


def n_bridges(v):
    return len(edges[v] & B)


# No idea how this works... credit to u/4HbQ
while sum((n_bridges(v) for v in A)) != 3:
    most_connected = max(A, key=n_bridges)
    A.remove(most_connected)
    B.add(most_connected)

answer1 = len(A) * len(B)
print(answer1)
