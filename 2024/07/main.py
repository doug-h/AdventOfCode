import re
import math

def valid_forms(target,values):

    forms = [values]
    for _ in range(len(values)-1):
        new_forms = []
        for f in forms:
            sl,l,*v,= f
            new_forms += [[sl+l,*v]]
            new_forms += [[sl*l,*v]]
            new_forms += [[int(str(sl)+str(l)),*v]]
        forms = new_forms
    return len([f[0] for f in forms if f[0] == target])

with open('input.txt') as file:
    eqs = file.read().splitlines()
    eqs = [list(map(int, re.findall(R"(\d+)", e))) for e in eqs]
    answer1 = sum(e[0] for e in eqs if valid_forms(e[0], e[1:]) != 0)
    print(answer1)
