with open("input.txt") as file:
    warehouse, moves = file.read().split("\n\n")

    warehouse = warehouse.splitlines()
    W,H = len(warehouse[0]),len(warehouse)
    warehouse = list("".join(warehouse))

    moves = "".join(moves.split('\n'))

    markers = "^>v<"
    warps = [-W,1,W,-1]
    dirs = dict(zip(markers, warps))
    pos = warehouse.index('@')
    warehouse[pos] = '.'
    for m in moves:
        i,j = pos%W,pos//W
        d = dirs[m]
        first_wall = pos+d*(1+warehouse[pos+d::d].index('#'))
        first_space = 0
        try:
            first_space = pos+d*(1+warehouse[pos+d:first_wall:d].index('.'))
        except ValueError:
            first_space = None
        if(first_space != None):
            warehouse[pos+d:first_space+d:d] = warehouse[pos:first_space:d]
            pos += d
    gps = 0
    for index in range(W*H):
        i,j = index%W,index//W
        if(warehouse[index] == 'O'):
            gps += i+j*100
    print(gps)
