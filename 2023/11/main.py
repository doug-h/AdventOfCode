
board = [line for line in open("data.txt").read().split('\n')[:-1]]

def answer(inc):
    stars = [[x, y] for y, line in enumerate(board)
             for x, c in enumerate(line) if c == '#']
    
    for y,row in reversed(list(enumerate(board))):
        if not '#' in row:
            if all((y != py for (px,py) in stars)):
                for s in stars:
                    if s[1] > y:
                        s[1] += (inc-1)
    
    for x,col in reversed(list(enumerate(zip(*board)))):
        if not '#' in col:
            if all((x != px for (px,py) in stars)):
                for s in stars:
                    if s[0] > x:
                        s[0] += (inc-1)
    
    distances = list(abs(p2[1]-p1[1]) + abs(p2[0]-p1[0]) for p1 in stars for p2 in stars if p1 != p2)
    return int(sum(distances)/2)

answer1 = answer(2)
answer2 = answer(1000000)

print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

assert (answer1 == 9565386)
assert (answer2 == 857986849428)
