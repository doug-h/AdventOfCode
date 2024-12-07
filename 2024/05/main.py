import functools

with open('input.txt') as file:
    rules, lines = file.read().split("\n\n")
    lines = [[a for a in r.split(',')] for r in lines.splitlines()]
    find = lambda a,b: -1 if a+'|'+b in rules else 1

    slines = [sorted(line, key=functools.cmp_to_key(find)) for line in lines]
    answer1 = sum(int(line[len(line)//2]) for line,sline in zip(lines, slines) if line == sline)
    answer2 = sum(int(sline[len(sline)//2]) for line,sline in zip(lines, slines) if line != sline)
    print(answer1,answer2)
