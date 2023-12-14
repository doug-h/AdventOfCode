import copy

_input = [block.split('\n')
          for block in open("data.txt").read().split('\n\n')[:-1]]


def print_v(b):
    for x in b:
        print(x)
    print()


def find_hor_mirrors(block):
    mirrors = []
    for i, row in enumerate(block[:-1]):
        width = min(i+1, len(block)-i-1)
        before = list(reversed(block[i-width+1:i+1]))
        after = block[i+1: i+width+1]
        equality = [b == a for br, ar in zip(
            before, after) for b, a in zip(br, ar)]
        if all(equality):
            mirrors.append(i)
    return mirrors


def find_smudges(block):
    smudges = []
    for i, row in enumerate(block[:-1]):
        width = min(i+1, len(block)-i-1)
        before = list(reversed(block[i-width+1:i+1]))
        after = block[i+1: i+width+1]
        equality = [b == a for br, ar in zip(
            before, after) for b, a in zip(br, ar)]
        if equality.count(False) == 1:
            almost_idx = equality.index(False)
            x, y = i-(almost_idx // len(row)), (almost_idx % len(row))
            smudges.append((x, y))
    return smudges


def do_both_ways(fn, block):
    mh = fn(block)
    block = list(zip(*block))
    mv = fn(block)
    return (mv, mh)


answer = 0
for block in _input:
    ms_old = do_both_ways(find_hor_mirrors, block)
    smudges = do_both_ways( find_smudges, block)
    if(smudges[0]):
        s0,s1 = smudges[0][0]
    else:
        s1,s0 = smudges[1][0]

    c = block[s1][s0]
    print_v(block)
    block[s1] = block[s1][:s0] + "#."[c == '#'] + block[s1][s0+1:]
    print_v(block)

    ms = do_both_ways(find_hor_mirrors, block)
    print(ms)
    for i, score in enumerate((1, 100)):
        for m in ms[i]:
            if m not in ms_old[i]:
                answer += (m+1)*score

print(answer)

assert (answer == 35521)
