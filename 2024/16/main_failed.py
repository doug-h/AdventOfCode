from collections import deque

with open("input.txt") as file:
    grid = file.read().splitlines()
    w,h = len(grid[0]),len(grid)
    grid = "".join(grid)

    distances = [-1 for _ in grid]
    start = grid.find('S')
    end = grid.find('E')

    dirs = N,E,S,W = [-w,1,w,-1]
    to_visit = deque()
    to_visit.append((start,0,E,[start]))
    seen = set()
    best_tiles = set([start])

    while to_visit:
        p,d,b,hist = to_visit.popleft()
        if p == end:
            print(d)
            best_tiles.update(hist)
            seen.update((end, a) for a in dirs)
            continue
        seen.add((p,b))
        first_wall = p+b*(1+grid[p+b::b].index('#'))
        path = grid[p+b:first_wall:b]
        hist2 = list(hist)
        for i,pi in enumerate(range(p+b,first_wall,b)):
            hist2.append(pi)
            if (pi,b) not in seen:
                to_visit.append((pi,d+1+i,b,list(hist2)))
        to_visit += [(p+a,d+1000+1,a,hist+[p+a]) for a in dirs if a != b and (p+a,a) not in seen and grid[p+a] != '#']
    print(len(best_tiles))
