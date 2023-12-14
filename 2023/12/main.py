
import functools


@functools.cache
def step(string, runs):
    run, *next_runs = runs
    result = 0

    for s_idx in range(0, len(string) - sum(runs) - len(runs) + 2):
        candidate, rest = string[s_idx:s_idx+run], string[s_idx+run:]
        if not '.' in candidate and not(len(rest) and rest[0] == '#'):
            if not next_runs:
                if not '#' in rest:
                    result += 1
            else:
                result += step(rest[1:], tuple(next_runs))
        if candidate[0] == '#':
            break
    return result


_input = [line.split() for line in open("data.txt")]
_input = [[s, tuple(int(i) for i in group.split(','))] for s, group in _input]

answer1 = sum(step(string, runs) for string, runs in _input)
_input = [('?'.join([string]*5), runs*5) for string, runs in _input]
answer2 = sum(step(string, runs) for string, runs in _input)


print(f"Part one: {answer1}")
assert (answer1 == 7110)
print(f"Part two: {answer2}")
assert (answer2 == 1566786613613)
