with open("input.txt") as file:
    s = file.read().rstrip()
    ID = 0
    expanded = []
    space = False
    for c in s:
        if not space:
            expanded += [str(ID)]*int(c)
            ID += 1
        else:
            expanded += ['.']*int(c)
        space = not space

    blocks = list(i for i in reversed(range(len(expanded))) if expanded[i] != '.')

    for block in blocks:
        first_space = expanded.index('.')
        if(first_space > block):
            break
        expanded[block],expanded[first_space] = expanded[first_space],expanded[block]
    answer1 = sum(int(c)*i for i,c in enumerate(expanded) if c != '.')
    
    files = [[ID,int(size),int(gap)] for (ID,size),gap in zip(enumerate(s[::2]), s[1::2]+"0")]

    for ID in reversed(range(len(files))):
        i,src = next((i,x) for i,x in reversed(list(enumerate(files))) if x[0] == ID)
        for j,dest in enumerate(files[:i]):
            if dest[2] >= src[1]:
                files[i-1][2] += src[1] + src[2]
                src[2] = dest[2] - src[1]
                dest[2] = 0
                files.pop(i)
                files.insert(j+1, src)
                break

    pos = 0
    answer2 = 0
    for (ID,size,gap) in files:
        for _ in range(size):
            answer2 += ID*pos
            pos += 1
        pos += gap

    print(answer1,answer2)

