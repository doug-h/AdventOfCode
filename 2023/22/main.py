blocks = [
    list(map(int, line.rstrip().replace("~", ",").split(",")))
    for line in open("data.txt")
]

blocks = sorted(blocks, key=lambda x: x[2])
highest_seen = {}
sitting_on = []
structural = set()
for i, b in enumerate(blocks):
    h = b[5] - b[2]

    floor = [
        highest_seen[x + y * 1j]
        for y in range(b[1], b[4] + 1)
        for x in range(b[0], b[3] + 1)
        if (x + y * 1j) in highest_seen
    ]
    new_z = max([c[0] for c in floor] + [0]) + 1

    floor = [f[1] for f in floor if f[0] == new_z - 1]
    sitting_on.append(set(floor))

    if len(sitting_on[-1]) == 1:
        structural.add(floor[0])

    b[2] = new_z
    b[5] = new_z + h

    for y in range(b[1], b[4] + 1):
        for x in range(b[0], b[3] + 1):
            highest_seen[x + y * 1j] = (b[5], i)

sat_on_by = [
    set(j for j, s in enumerate(sitting_on) if i in s) for i in range(len(blocks))
]


def count(start):
    fallen = set()
    to_visit = [start]
    while to_visit:
        s = to_visit.pop()
        fallen.add(s)
        to_visit.extend(
            v for v in sat_on_by[s] if all(a in fallen for a in sitting_on[v])
        )

    return len(fallen) - 1


answer1 = len(blocks) - len(structural)
answer2 = sum((count(s) for s in structural))

print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

assert answer1 == 459
assert answer2 == 75784
