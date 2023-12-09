import itertools

answer1 = answer2 = 0
for line in open("data.txt").read().split('\n')[:-1]:
    values = [[int(v) for v in line.split()]]
    while any(v != 0 for v in values[-1]):
        values.append([b-a for (a, b) in itertools.pairwise(values[-1])])
    answer1 += sum(v[-1] for v in values)
    answer2 += sum((a[0]-b[0] for (a, b) in zip(values[::2], values[1::2])))

print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

assert (answer1 == 1930746032)
assert (answer2 == 1154)
