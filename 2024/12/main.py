from collections import Counter

with open("input.txt") as file:
    s = file.read().splitlines()
    W,H = len(s[0]), len(s)
    original_grid = "".join(s)

    unique_grid = [0] * (W*H)
    
    unvisited = set(range(W*H))
    to_visit = set()
    ID = 0
    old_labels = ['X']
    while unvisited:
        if to_visit:
            index = to_visit.pop()
            unvisited.remove(index)
        else:
            ID += 1
            index = unvisited.pop()
            old_labels.append(original_grid[index])

        plot = original_grid[index]
        i,j = index%W,index//W

        unique_grid[index] = ID

        for ni,nj in (i+1,j),(i-1,j),(i,j+1), (i,j-1):
            if ni < 0 or nj < 0 or ni >= W or nj >= H:
                continue
            nindex = ni+nj*W
            neighbour = original_grid[nindex]
            if neighbour == plot and nindex in unvisited:
                to_visit.add(nindex)


    areas = Counter(unique_grid)
    perms = Counter()
    corns = Counter()
    for index in range(W*H):
        i,j = index%W,index//W
        ID = unique_grid[index]

        neighbours = [(i-1,j), (i,j-1),(i+1,j),(i,j+1)]
        corners = [(i-1,j-1),(i+1,j-1),(i+1,j+1),(i-1,j+1)]
        in_bounds = lambda ni,nj: (ni >= 0 and nj >= 0 and ni < W and nj < H)
        IDs = [unique_grid[ni+nj*W] if in_bounds(ni,nj) else -1 for ni,nj in neighbours]

        IDs.append(IDs[0])

        for ID0,ID1,(ci,cj) in zip(IDs[:-1],IDs[1:],corners):
            if ID0 != ID:
                perms[ID] += 1
                if ID1 != ID:
                    corns[ID] += 1
                if ID0 == ID1 and ID0 != -1 and unique_grid[ci+cj*W] == ID0:
                    corns[unique_grid[ci+cj*W]] += 1

    answer1 = 0
    answer2 = 0
    for ID in set(unique_grid):
        answer1 += areas[ID]*perms[ID]
        answer2 += areas[ID]*corns[ID]
    print(answer1,answer2)

