board = {
    a + b * 1j: c for b, row in enumerate(open("data.txt")) for a, c in enumerate(row)
}

board[65 + 65j] = "."

# NOTE - Outer rim of garden  and corridor north/south/east/west from start
# are all '.', so whatever cell we enter the garden from will eventually
# become a fully flooded garden, if there are enough steps. This means the
# bulk of the infinite garden are all the same, we only have to care about the borders
# This also means the step we reach each garden is entirely predicatble:
# 	start walking directly to the right, if gardens are 131 steps wide then we will reach the border after 65 steps
# 	We hit the first cell of the next garden after 66 steps, no other path could have got here sooner.
# 	That path spreads out, and because the outer rim is all empty, we spread faster than any other path could have.
# 	e.g. every cell on the border of every garden we reach in the minimum number of steps from the origin
# 	It also means the first cell we reach of every garden is the center of a wall if we are directly N/S/E/W of the origin
# or otherwise the corner. Therefore we can just calculate the flood from the eight possible start points

# The total number of cells of a full garden alternates between 7556 and 7602
# The rocks are sparse, e.g. no part of the garden takes longer to fill than the border, it takes 260 to fill from any corner, and 195 from any edge
# N = 26501365 == 202300 * 131 + 65, so we go 202300 gardens in every cardinal direction, finishing at the far wall,
# the closest point of those gardens is D = 202300*131 - 65 away, so we have N - D = 130 steps left to flood them
# There are two rings of diagonal gardens, one with 64 steps to flood and one with 195
# As the garden size is odd (131) the walkable cells will flip between gardens (checkerboard pattern)


def walk(start, max_n=10000):
    seen = set([start])
    frontier = [start]

    tiles = [0, 0, 1]

    i = 0
    for i in range(max_n):
        to_step = [x for x in frontier]

        frontier = []
        while to_step:
            f = to_step.pop(0)

            for d in [1, -1, 1j, -1j]:
                p = f + d
                p_m = p + 65 + 65j

                if p_m in board and p not in seen and board[p_m] == ".":
                    seen.add(p)
                    frontier.append(p)
        if len(frontier) == 0:
            break
        tiles.append(tiles[-2] + len(frontier))
    return tiles[2:]

corners = [-65-65j, 65-65j, -65+65j, 65+65j]
edges = [-65,65,-65j,65j]
start_points = [0, *corners, *edges]

flood_amounts = [walk(start_point) for start_point in start_points]

def get_tile_count(start_point, n_steps):
    a = flood_amounts[start_points.index(start_point)]
    if n_steps < len(a):
        return a[n_steps]
    else:
        n = n_steps - len(a)
        return a[(n % 2) - 2]


N = 26501365
W = 131
skip = N // W
hW = W // 2


even_filled = (skip - 1) * (skip - 1) * get_tile_count(0, N)
odd_filled = (skip) * (skip) * get_tile_count(65, N - 66)
tips = sum((get_tile_count(c, 130) for c in edges))
inner_diagonals = sum(
    (
        (skip - 1) * get_tile_count(c, 195)
        for c in corners
    )
)
outer_diagonals = sum(
    ((skip) * get_tile_count(c, 64) for c in corners)
)

answer1 = flood_amounts[0][64]
answer2 = even_filled + odd_filled + tips + inner_diagonals + outer_diagonals


print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

assert (answer1 == 3724)
assert (answer2 == 620348631910321)
