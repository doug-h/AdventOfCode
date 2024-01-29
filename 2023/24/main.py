import itertools
import math

# The numbers in the input are integers with 14/15 significant figures
# The largest numbers (around 4E14) are getting close to the double limit
# e.g. 486606029656616.xx can only have fractional parts of 1/16, 2/16,...
# In general, doing maths with these large numbers should cause problems,
# but I seem to have got lucky here


def add(v1, v2):
    return [a + b for a, b in zip(v1, v2)]


def sub(v1, v2):
    return [a - b for a, b in zip(v1, v2)]


def mult(v, s):
    return [a * s for a in v]


def mag(v):
    return math.sqrt(dot(v, v))


def dot(v1, v2):
    return sum([a * b for a, b in zip(v1, v2)])


def cross2(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


def cross3(v1, v2):
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0],
    ]


data = [
    [list(map(int, p.strip().split(",")[:])) for p in line.split("@")]
    for line in open("data.txt")
]

minp = (200000000000000, 200000000000000)
maxp = (400000000000000, 400000000000000)

answer1 = 0
for (p1, v1), (p2, v2) in itertools.combinations(data, 2):
    d1 = add(p1, v1)
    d2 = add(p2, v2)

    v1_X_v2 = cross2(v1, v2)
    P = add(mult(v1, cross2(p2, d2)), mult(v2, -cross2(p1, d1)))

    if v1_X_v2 == 0:
        continue  # print("Never meet", p1, v1, p2, v2)
    else:
        P = mult(P, 1 / v1_X_v2)
        s1, s2 = dot(sub(P, p1), v1[:2]), dot(sub(P, p2), v2[:2])
        if s1 < 0 or s2 < 0:
            continue  # print("Past", P)
        elif minp[0] <= P[0] <= maxp[1] and minp[1] <= P[1] <= maxp[1]:
            # print("Inside", P)
            answer1 += 1
        else:
            continue  # print("Outside", P)

# We need to work out the times the hailstones hit our rock at, and the line of the rock itself
# This is 6(N+1) unknowns, but clearly the system is constrained
# If we find two hailstones with distinct positions and non-parallel velocities we can define a plane
# in the reference frame of one of the stones. The rock path must lie in that plane.
# Then we can add another distinct non-planar hailstone to reduce the plane to a line.

# Find the first three hailstones that satisfy ^^^
h1 = data[0]
h2 = 0
h3 = 0
for h2 in data[1:]:
    if h1[0] != h2[0] and cross2(h1[1], h2[1]) != 0:
        break

for h3 in data[2:]:
    if h1[0] != h3[0] and h2[0] != h3[0] and dot(h3[1], cross3(h1[1], h2[1])) > 0.001:
        break


# convert to h1's frame
p2 = sub(h2[0], h1[0])
p3 = sub(h3[0], h1[0])
v2 = sub(h2[1], h1[1])
v3 = sub(h3[1], h1[1])

N = cross3(p2, v2)

t3 = -dot(p3, N) / dot(v3, N)
intersection = add(p3, mult(v3, t3))

t2 = cross2(intersection, p2) / cross2(v2, intersection)

c2 = add(h2[0], mult(h2[1], t2))
c3 = add(h3[0], mult(h3[1], t3))
print(f"Rock collides with h2 after {round(t2)}s at {list(map(round,c2))}")
print(f"Rock collides with h3 after {round(t3)}s at {list(map(round,c3))}")
dt = t3 - t2
dp = sub(c3, c2)
v_rock = mult(dp, 1 / dt)
p_rock = sub(c2, mult(v_rock, t2))

print(f"Extrapolating start to {p_rock}")
answer2 = round(sum(p_rock))

print(answer1)
print(answer2)

assert answer1 == 15318
assert answer2 == 870379016024859
