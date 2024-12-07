def pattern(grid): 
    grid = list(grid)
    cs = [-1j, 1, 1j, -1]

    start = grid.index('^')
    pos = complex(start%W, start//W)
    d = 0
    visited = {}
    while(True):
        h = visited.get(pos)
        if h:
            if d in h:
                return True,visited
            visited[pos].add(d)
        else:
            visited[pos] = set([d])

        next_pos = pos+cs[d]
        if next_pos.real < 0 or next_pos.real >= W or next_pos.imag < 0 or next_pos.imag >= H:
            break
        if(grid[index(next_pos)] == '#'):
            d = (d+1)%4
        else:
            pos = next_pos

    return False,visited

with open('input.txt') as file:
    grid = file.read().splitlines()
    W,H = len(grid[0]), len(grid)
    grid = list("".join(grid))
    index = lambda p : int(p.imag*W + p.real)

    cs = [-1j, 1, 1j, -1]

    _,poss= pattern(grid)

    answer1 = len(poss)
    start = grid.index('^')
    del poss[complex(start%W, start//W)]

    answer2 = 0
    for p in poss:
        l = list(grid)
        l[index(p)] = '#'
        loops,_ = pattern(l)
        answer2 += loops
    print(answer1,answer2)

