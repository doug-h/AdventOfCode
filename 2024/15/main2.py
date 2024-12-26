def can_move(pos, d):
    match warehouse[pos]:
        case '#':
            return False
        case '.':
            return True
        case '[':
            return can_move(pos+d,d) and (d == left or d == right or can_move(pos+d+1,d))
        case ']':
            return can_move(pos+d,d) and (d == left or d == right or can_move(pos+d-1,d))
    assert(0)

def move(pos, d):
    match warehouse[pos]:
        case '#':
            assert(0)
        case '.':
            return
        case '[':
            pair = pos+1
            #Move blockers
            if d != left:
                move(pair+d,d)
            if d != right:
                move(pos+d,d)
            warehouse[pos] = '.'
            warehouse[pair] = '.'
            warehouse[pos+d] = '['
            warehouse[pair+d] = ']'
        case ']':
            pair = pos-1
            #Move blockers
            if d != left:
                move(pos+d,d)
            if d != right:
                move(pair+d,d)
            warehouse[pos] = '.'
            warehouse[pair] = '.'
            warehouse[pos+d] = ']'
            warehouse[pair+d] = '['

with open("input.txt") as file:
    expand = dict(zip("#O.@",["##","[]","..","@."]))
    expand = str.maketrans(expand)
    warehouse, moves = file.read().split("\n\n")

    warehouse = warehouse.translate(expand)
    warehouse = warehouse.splitlines()
    W,H = len(warehouse[0]),len(warehouse)
    warehouse = list("".join(warehouse))

    moves = "".join(moves.split('\n'))

    markers = "^>v<"
    warps = [-W,1,W,-1]
    up,right,down,left = warps
    dirs = dict(zip(markers, warps))
    pos = warehouse.index('@')
    warehouse[pos] = '.'
    for m in moves:
        i,j = pos%W,pos//W
        d = dirs[m]
        if can_move(pos+d,d):
            move(pos+d,d)
            pos += d
    gps = 0
    for index in range(W*H):
        i,j = index%W,index//W
        if(warehouse[index] == '['):
            gps += i+j*100
    print(gps)
