import functools

@functools.cache
def paths(start_x, start_y, end_x, end_y):
    if(start_x == end_x and start_y == end_y):
        return 1

    height = -1 if grid[start_y*W+start_x] == '.' else int(grid[start_y*W+start_x])
    start = complex(start_x, start_y)

    count = 0
    for (x,y) in [(int(n.real),int(n.imag)) for d in [1,-1,1j,-1j]
                  if (n := start+d).real >= 0 and
                  n.real < W and
                  n.imag >= 0 and
                  n.imag < H and
                  grid[int(n.imag)*W+int(n.real)]==str(height+1)]:
        count += paths(x,y,end_x,end_y)
    return count



def update_flood(height,poss):
    next_poss = set()
    for p in poss:
        flood[int(p.imag)][int(p.real)] += 1
        for neighbour in [n for d in [1,-1,1j,-1j] if (n := p+d).real >= 0 and
                          n.real < W and
                          n.imag >= 0 and
                          n.imag < H and
                          grid[int(n.imag)*W+int(n.real)]==str(height-1)]:
            next_poss.add(neighbour)
    if(height > 0):
        update_flood(height-1,next_poss)

with open("input.txt") as file:
    strings = file.read().splitlines()
    W,H = len(strings[0]), len(strings)

    flood = [[0]*W for _ in range(H)]

    grid = "".join(strings)
    for row in range(H):
        for col in range(W):
            index = row*W + col
            if(grid[index] == '9'):
                update_flood(9, [complex(col, row)])
    #answer1 = sum(flood[row][col]
    #              for row in range(H)
    #              for col in range(W)
    #              if grid[row*W+col] == '0')
    #print(answer1)
    inds_0 = [(i,j) for i in range(W) for j in range(H) if grid[j*W+i] == '0']
    inds_9 = [(i,j) for i in range(W) for j in range(H) if grid[j*W+i] == '9']
    answer2 = sum(paths(*p0,*p9) for p0 in inds_0 for p9 in inds_9)
    print(answer2)

