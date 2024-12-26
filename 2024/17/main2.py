import re

def check(A,target):
    B = A%8 #2,4
    B ^= 5 #1,5
    C = A >> B #7,5
    B ^= 6 #1,6
    B ^= C
    return (B%8) == target

with open("input.txt") as file:
    regs, prog = file.read().split('\n\n')
    program = [int(d) for d in re.findall(R"(\d+)", prog)]

    todo = [(0,program)]
    while(todo):
        val,rem = todo.pop()
        if not rem:
            print(val>>3)
            break
        todo += [((val+a)<<3,rem[:-1]) for a in reversed(range(8)) if check(val+a,rem[-1])]
