import re,math

with open("input.txt") as file:
    W = 101 
    H = 103

    robots = [list(map(int,re.match(R"p\=(-?\d+),(-?\d+) v\=(-?\d+),(-?\d+)", m).groups())) for m in file.read().splitlines()]
    robots = [([px,py],(vx,vy)) for px,py,vx,vy in robots]

    start = 7241+103
    step_size = 1
    num_steps = 0
    for p,v in robots:
        p[0] += v[0] * start
        p[1] += v[1] * start
        p[0] %= W
        p[1] %= H
    for step in range(num_steps):
        for p,v in robots:
            p[0] += v[0] * step_size
            p[1] += v[1] * step_size
            p[0] %= W
            p[1] %= H

        grid = [0 for _ in range(W*H)]
        for j in range(H):
            for i in range(W):
                grid[j*W+i] = sum(1 for p,v in robots if p[0] == i and p[1] == j)
        print()
        print()
        print()
        print(start+step*step_size)
        for j in range(H):
            for i in range(W):
                g = grid[i+j*W]
                print(g if g else '.', end = '')
            print()


    quads = [0,0,0,0]
    for p,_ in robots:
        qx = p[0] - (W//2)
        qy = p[1] - (H//2)
        if qx == 0 or qy == 0:
            continue
        quads[(qx > 0) + (qy > 0)*2] += 1

    print(math.prod(quads))

