import itertools

board = ['.'+line+'.' for line in open("data.txt").read().split('\n')[:-1]]
board = ["."*len(board[0])] + board + ["."*len(board[0])]

distances = [[0]*len(board[0]) for _ in range(len(board))]

directions = {}
directions['S'] = ((0, -1), (0, 1), (1, 0), (-1, 0))
directions['|'] = ((0, -1), (0, 1))
directions['-'] = ((-1, 0), (1, 0))
directions['L'] = ((0, -1), (1, 0))
directions['J'] = ((0, -1), (-1, 0))
directions['7'] = ((-1, 0), (0, 1))
directions['F'] = ((1, 0), (0, 1))
directions['.'] = ()


def find_S():
    for y in range(len(board)):
        for x in range(len(board[0])):
            if (board[y][x] == 'S'):
                return x, y


def find_direction(x, y):
    for j in range(max(0, y-1), min(len(board), y+2)):
        for i in range(max(0, x-1), min(len(board[0]), x+2)):
            if not distances[j][i] \
                    and any((x+d[0], y+d[1]) == (i, j) for d in directions[board[y][x]]) \
                    and any((x, y) == (i+d[0], j+d[1]) for d in directions[board[j][i]]):
                return i, j


def print_v(ds):
    for v in ds:
        print(v)
    print()

#  ========= The actual algorithm =========
x, y = find_S()
distance = 1
while not distances[y][x]:
    distances[y][x] = distance
    s = find_direction(x, y)
    if s:
        x, y = s
        distance += 1
    else:
        break
distances = [[min(distance+2-d, d) for d in row] for row in distances]
answer1 = max(d for row in distances for d in row)-1
# =========================================


# Replace 'S' with the character it's supposed to be
x, y = find_S()
for c, ds in directions.items():
    if c == 'S':
        continue
    if all((distances[y+d[1]][x+d[0]] == 2) for d in ds):
        s = list(board[y])
        s[x] = c
        board[y] = ''.join(s)
        break


# Winding number style check for interior
def ray_check(x, y):
    if (distances[y][x] != 0):
        return 0
    n_intersections = 0
    j = y
    for i in range(x, len(board[0])):
        if distances[j][i] == 0: continue
        c = board[j][i]
        if c in ['|', 'L', 'J']:
            n_intersections += 1
    return n_intersections % 2


interior = [[ray_check(x, y) for x in range(len(board[0]))]
            for y in range(len(board))]
answer2 = (sum((i for row in interior for i in row)))

# out_board = [''.join(['I' if interior[j][i] else board[j][i]
#               for i in range(len(board[0]))]) for j in range(len(board))]



print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

assert (answer1 == 6867)
assert (answer2 == 595)
