import math

board = {
    a + b * 1j: c for b, row in enumerate(open("data.txt")) for a, c in enumerate(row)
}


start = 1
end = 139 + 140j


# ============ Build graph ===============
verts = [start]

# Start, End, Length
edges = [[0, -1, -1]]
queue = [(start, 0)]
visited = set()

while queue:
    q, eidx = queue.pop(0)
    edges[eidx][2] += 1
    visited.add((q, eidx))
    neighbours = [
        [q + d, eidx]
        for d, s in zip([-1j, 1j, 1, -1], "^v><")
        if q + d in board and board[q + d] in (".", s)
    ]
    if board[q] == "." and all(board[c[0]] in "^v><" for c in neighbours):
        if q in verts:
            edges[eidx][1] = verts.index(q)
            continue

        edges[eidx][1] = len(verts)
        verts.append(q)
        for i, n in enumerate(neighbours):
            neighbours[i][1] = len(edges)
            edges.append([edges[eidx][1], -1, 0])
            visited.add((q, neighbours[i][1]))
    queue.extend([s for s in neighbours if tuple(s) not in visited])

# Assume no dead ends
verts.append(end)
for i in range(len(edges)):
    if edges[i][1] == -1:
        edges[i][1] = len(verts) - 1

neighbours = [[] for _ in verts]
for i, v in enumerate(verts):
    neighbours[i].extend([(e[1], e[2]) for e in edges if e[0] == i])
    neighbours[i] = sorted(neighbours[i], key=lambda x: -x[1])

# =========== Part One ============
# Input is an acyclic directed graph, so this is simple
distances = [math.inf for v in verts]
distances[0] = 0

queue = [0]
while queue:
    q = queue.pop(0)
    for v, w in [e[1:] for e in edges if e[0] == q]:
        dist = distances[q] - w
        if dist < distances[v]:
            queue.append(v)
            distances[v] = dist
answer1 = -distances[-1]
# =================================


for i, v in enumerate(verts):
    neighbours[i].extend([(e[0], e[2]) for e in edges if e[1] == i])
    neighbours[i] = sorted(neighbours[i], key=lambda x: -x[1])

# =========== Part Two ============
stack = [(0, 0, [])]
max_d = answer1
while stack:
    vert, dist, visited = stack.pop()
    for v, w in neighbours[vert]:
        if v == len(verts) - 1:
            max_d = max(max_d, dist + w)
            if max_d == dist + w:
                print(max_d)
        elif v not in visited:
            new_visitied = visited + [v]
            stack.append((v, dist + w, new_visitied))
answer2 = max_d
# =================================

print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

# assert answer1 == 459
# assert answer2 == 75784
