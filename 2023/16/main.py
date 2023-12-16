
import sys
board = open("data.txt").readlines()
board = [s.rstrip() for s in board]


def print_v(v):
    for x in v:
        print(x)
    print()


east, south, west, north = range(4)


dirs = [1, 0+1j, -1, 0-1j]
visited = [[[False for _ in dirs] for c in row] for row in board]


stack = []


def flood(p, heading):
    if p.real < 0 or p.imag < 0 or p.real >= len(board[0]) or p.imag >= len(board):
        return
    if visited[int(p.imag)][int(p.real)][heading] == True:
        return
    visited[int(p.imag)][int(p.real)][heading] = True
    c = board[int(p.imag)][int(p.real)]

    if c == '.':
        stack.append((p+dirs[heading], heading))
        return

    match heading:
        case 0: # east
            if c == '/' or c == '|':
                stack.append((p+dirs[north], north))
            if c == '\\' or c == '|':
                stack.append((p+dirs[south], south))
            if c == '-':
                stack.append((p+dirs[heading], heading))
            return
        case 1: # south
            if c == '/' or c == '-':
                stack.append((p+dirs[west], west))
            if c == '\\' or c == '-':
                stack.append((p+dirs[east], east))
            if c == '|':
                stack.append((p+dirs[heading], heading))
            return
        case 2: # west
            if c == '/' or c == '|':
                stack.append((p+dirs[south], south))
            if c == '\\' or c == '|':
                stack.append((p+dirs[north], north))
            if c == '-':
                stack.append((p+dirs[heading], heading))
            return
        case 3: # north
            if c == '/' or c == '-':
                stack.append((p+dirs[east], east))
            if c == '\\' or c == '-':
                stack.append((p+dirs[west], west))
            if c == '|':
                stack.append((p+dirs[heading], heading))
            return


answers = []
def stack_flood(p, d):
    global visited, stack, answers
    visited = [[[False, False, False, False] for c in row] for row in board]
    stack = [(p, d)]
    while len(stack):
        s = stack.pop()
        flood(*s)
    answer = [1 for row in visited for v in row if any(v)]
    answers.append(len(answer))



for i in range(len(board)):
    stack_flood(1j*i, east)
    stack_flood(len(board)-1+1j*i, west)
for i in range(len(board[0])):
    stack_flood(i, south)
    stack_flood(len(board)-1+i, north)


answer1 = answers[0]
answer2 = max(answers)


print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

assert (answer1 == 7939)
assert (answer2 == 8318)
