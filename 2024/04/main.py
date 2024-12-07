with open('input.txt') as file:
    grid = file.read()
    w,N = grid.find('\n')+1, len(grid)
    grid += '\n' * 2 * w

    dirs = [1,w,(w+1),(w-1)]
    answer1 = sum(sum(grid[i-d::d].startswith(("XMAS", "SAMX")) for d in dirs) for i in range(N))
    answer2 = sum(all(grid[i-d::d].startswith(("MAS", "SAM")) for d in dirs[2:]) for i in range(N))
    print(answer1, answer2)

#2434
#1835
