import functools

@functools.cache
def possibilities(d):
    if d == '':
        return 1

    return sum(possibilities(d[i+1:]) for i in range(len(d)) if d[:i+1] in patterns)

with open("input.txt") as file:
    patterns, designs = file.read().split('\n\n')
    patterns = set(patterns.split(", "))

    ps = [possibilities(d) for d in designs.splitlines()]
    print(sum(map(bool,ps)),sum(ps))
