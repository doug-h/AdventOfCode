def full_walk(start_index, start_dir):
    assert(grid[start_index] != '#')

    d = start_dir
    i = start_index

    visited = []
    while(True):
        jump = blocks[d][i]
        if jump == -1:
            limit = [i%W,i-(i%W)+W-1,i%W+W*(H-1),i-(i%W)]
            visited += [(di,d) for di in range(i,limit[d]+warps[d],warps[d])]
            return False, visited

        visited += [(di,d) for di in range(i,jump,warps[d])]
        i = jump - warps[d]
        d = (d+1)%4


def loops(start_index, start_dir, extra_block_index):
    assert(grid[start_index] != '#')

    d = start_dir
    i = start_index

    visited = set()
    while(True):
        if (i,d) in visited:
            return True

        jump = blocks[d][i]
        limit = [i%W,i-(i%W)+W-1,i%W+W*(H-1),i-(i%W)]
        if((jump != -1 and extra_block_index in range(i, jump, warps[d])) or 
           (jump == -1 and extra_block_index in range(i, limit[d]+1, warps[d]))):
            #print(jump%W,jump//W, extra_block_index%W, extra_block_index//W,"hit extra rock")
            jump = extra_block_index
        if jump == -1:
            limit = [i%W,i-(i%W)+W-1,i%W+W*(H-1),i-(i%W)]
            visited |= set((di,d) for di in range(i,limit[d]+warps[d],warps[d]))
            return False

        visited |= set((di,d) for di in range(i,jump,warps[d]))
        i = jump - warps[d]
        #print(i%W, i//W, d, "hit rock")
        d = (d+1)%4

with open('input.txt') as file:
    grid = file.read().splitlines()
    W,H = len(grid[0]), len(grid)
    grid = "".join(grid)

    warps = [-W,1,W,-1]

    start = grid.find('^')
    grid = grid[:start] + '.' + grid[start+1:]

    blocks = [[None for _ in range(W*H)] for _ in range(4)]
    for j in range(H):
        block = -1
        for i in range(W):
            index = j*W+i
            if grid[index] == '#':
                block = index
            blocks[3][index] = block
    for j in range(H):
        block = -1
        for i in reversed(range(W)):
            index = j*W+i
            if grid[index] == '#':
                block = index
            blocks[1][index] = block
    for i in range(W):
        block = -1
        for j in range(H):
            index = j*W+i
            if grid[index] == '#':
                block = index
            blocks[0][index] = block
    for i in range(W):
        block = -1
        for j in reversed(range(H)):
            index = j*W+i
            if grid[index] == '#':
                block = index
            blocks[2][index] = block

    _,path = full_walk(start,0)
    visited = set(di for di,_ in path)
    possible_poss = visited
    answer2 = 0
    for (p0,d0),(p1,d1) in zip(path[:-1],path[1:]):
        if p1 in possible_poss:
            possible_poss.discard(p1)
            loop = loops(p0,d0,p1)
            if loop:
                answer2 += 1
    print(answer2)


