_inputs = open("data.txt").read().split(',')
_inputs = [s.rstrip() for s in _inputs]


def _hash(string):
    value = 0
    for s in string:
        value += ord(s)
        value = (value * 17) % 256
    return value


boxes = [[] for _ in range(256)]

for i in _inputs:
    label = ""
    if len(eq := i.split('=')) > 1:
        label = eq[0]
        foc = int(eq[1])
        box = _hash(label)
        if (l := [lens for lens in boxes[box] if lens[0] == label]):
            i = boxes[box].index(l[0])
            boxes[box][i] = (label, foc)
        else:
            boxes[box].append((label, foc))

    elif len(sub := i.split('-')) > 1:
        label = sub[0]
        box = _hash(label)
        if (l := [lens for lens in boxes[box] if lens[0] == label]):
            boxes[box].remove(l[0])
    else:
        assert (0)


answer1 = sum(map(_hash, _inputs))
answer2 = sum((i+1)*sum((j+1)*lens[1] for j, lens in enumerate(box))
              for i, box in enumerate(boxes))

print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

assert(answer1 == 512797)
assert(answer2 == 262454)
