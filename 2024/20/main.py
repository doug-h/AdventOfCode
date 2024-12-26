def manhattan(index1,index2):
    return abs(index1%w-index2%w)+abs(index1//w-index2//w)

def cheats(cheat_length, min_skip):
    n = 0
    for i,p in enumerate(path):
        for j,q in enumerate(path[:i-min_skip-1]):
            path_dist = i - j
            grid_dist = manhattan(p,q)
            if grid_dist <= cheat_length and path_dist >= min_skip+grid_dist:
                n += 1
    return n

with open("input.txt") as file:
    grid = file.read().splitlines()
    w,h = len(grid[0]),len(grid)
    grid = "".join(grid)

    path = []
    seen = set()

    to_visit = [grid.find('S')]
    for p in to_visit:
        path.append(p)
        seen.add(p)
        to_visit += [p+a for a in [-w,1,w,-1] if grid[p+a] != '#' and (p+a) not in seen]

    print(cheats(2,100), cheats(20,100))
