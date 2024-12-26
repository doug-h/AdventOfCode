def fits(key,lock):
    for p1,p2 in zip(key,lock):
        if p1+p2 > 5:
            return False
    return True

with open("input.txt") as file:
    blocks = keys,locks = [[],[]]
    for B in open("input.txt").read().split('\n\n'):
        blocks[B[0]=='#'].append([B[i::6].count('#')-1 for i in range(5)])

    print(sum(fits(k,l) for k in keys for l in locks))
