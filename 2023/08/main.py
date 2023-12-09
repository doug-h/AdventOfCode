# Only cycles with length % len(instructions) == 0 should be correct
# (or over a smaller range e.g. LLRLLR)
# but the input has been chosen so this doesn't matter??
# Also every cycle starts on the index equal to the cycle length?
# eg cycle [c0-->c1] has c1-c0 == c0 ??
# Makes the problem a lot easier
# (at least compared to that bus problem from a couple years ago)

import math
import itertools


def path(p):
    for ins in itertools.cycle(instructions):
        p = routes[p][ins == 'R']
        yield p
        if p[-1] == 'Z':
            break


instructions, _, *paths, _ = open("data.txt").read().split('\n')
routes = {p[:3]: (p[7:10], p[12:15]) for p in sorted(paths)}
cycles = [len(list(path(p))) for p in routes.keys() if p[-1] == 'A']

answer1 = cycles[0]
answer2 = math.lcm(*cycles)
print(f"Part one: {answer1}")
print(f"Part two: {answer2}")
assert (answer1 == 16697)
assert (answer2 == 10668805667831)
