import re

def pathable(num_bytes):
    grid = [-1 for _ in range(W*H)]
    for x,y in bytes[:num_bytes]:
        grid[x+y*W] = '#'

    todo = [(0,0)]
    grid[0] = 0
    while(todo):
        pos,steps = todo.pop(0)
        i,j = pos%W,pos//W
        if(i == W-1 and j == H-1):
            return True
        neighbours = [(pos+a,steps+1) for a,b in zip(warps,[j>0,i<W-1,j<H-1,i>0]) if b and grid[pos+a]==-1]
        for n,s in neighbours:
            grid[n] = s
        todo += neighbours
    return False


with open("input.txt") as file:
    digits = [int(d) for d in re.findall(R"(\d+)", file.read())]
    bytes = list(zip(digits[::2], digits[1::2]))

    W,H = 71,71
    warps = [-W,1,W,-1]

    low,high = 0,len(bytes)
    while(low < high-1):
        mid = (low+high)//2
        if(pathable(mid)):
            low = mid
        else:
            high = mid
    print(bytes[low])
