
def print_v(v):
    for x in v:
        print(x)
    print()


def move_up(b):
    for y, row in enumerate(b):
        for x, col in enumerate(row):
            if col == 'O':
                first_hash = -1
                n_balls = 1
                for up in range(y-1, -1, -1):
                    if b[up][x] == '#':
                        first_hash = up
                        break
                    elif b[up][x] == 'O':
                        n_balls += 1
                new_y = first_hash+n_balls
                b[y][x] = '.'
                b[new_y][x] = 'O'


def rotate(b):
    return [list(z) for z in zip(*b[::-1])]


def weight(b):
    return sum(len(b) - y for y, row in enumerate(b) for x, c in enumerate(row) if c == 'O')


def cycle(b):
    for _ in range(4):
        move_up(b)
        b = rotate(b)
    return b


def part1():
    board = open("data.txt").read().split('\n')[:-1]
    board = list(map(list, board))
    move_up(board)
    return weight(board)


def part2(reps):
    board = open("data.txt").read().split('\n')[:-1]
    board = list(map(list, board))
    history = {}
    rep = (0, 0)
    for i in range(reps):
        str_board = ''.join(''.join(row) for row in board)
        if str_board in history:
            print("Repeated after ", i, " last seen at ", history[str_board])
            rep = (history[str_board], i)
            break
        else:
            history[str_board] = i
        board = cycle(board)
    remainder = (reps - rep[1]) % (rep[1]-rep[0])
    for _ in range(remainder):
        board = cycle(board)

    return weight(board)


answer1 = part1()
answer2 = part2(1000000)

print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

# assert(answer1 == 108813)
# assert(answer2 == 104533)
