import itertools,functools

@functools.cache
def length(start,end,d):
    ps = paths[start,end]
    if d == 0:
        return min(len(p) for p in ps)+1
    return min(sum(length(s,e,d-1) for s,e in zip('A'+c,c+'A')) for c in ps)


with open("input.txt") as file:
    codes = file.read().splitlines()

    numeric_keypad = ("789", "456", "123", " 0A")
    directional_keypad = (" ^A", "<v>")

    row = {'<':0,'>':0,'^':-1,'v':1}
    col = {'<':-1,'>':1,'^':0,'v':0}

    paths = {}
    for k in numeric_keypad,directional_keypad:
        for start_row in range(len(k)):
            for start_col in range(len(k[0])):
                start = k[start_row][start_col]
                if(start == ' '): continue
                for end_row in range(len(k)):
                    for end_col in range(len(k[0])):
                        end = k[end_row][end_col]
                        if(end == ' '): continue
                        di = end_col - start_col
                        dj = end_row - start_row
                        moves  = di*'>' if di > 0 else -di*'<'
                        moves += dj*'v' if dj > 0 else -dj*'^'
                        paths[start,end] = set("".join(p) for p in itertools.permutations(moves))
                        for p in set(paths[start,end]):
                            i,j = start_col,start_row
                            for c in p:
                                i += col[c]
                                j += row[c]
                                if(k[j][i] == ' '): paths[start,end].remove(p)
    for n in 2,25:
        print(sum(sum(length(s,e,n) for s,e in zip('A'+c,c))*int(c[:-1]) for c in codes))
