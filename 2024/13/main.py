import re

def dot(x1,y1,x2,y2):
    return x1*x2+y1*y2

def cross(x1,y1,x2,y2):
    return x1*y2-x2*y1

def add(x1,y1,x2,y2):
    return (x1+x2,y1+y2)

def mult(x,y,c):
    return (x*c,y*c)

with open("input.txt") as file:
    machines = file.read().split("\n\n")
    machines = [map(int,re.match(R"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X\=(\d+), Y\=(\d+)", m).groups()) for m in machines]
    machines = [((ax,ay), (bx,by), (px,py)) for ax,ay,bx,by,px,py in machines]

    costA = 3
    costB = 1

    for extra in [0,10000000000000]:
        score = 0
        for a,b,p in machines:
            p = add(*p,extra,extra)
            if(cross(*a,*b) == 0):
                assert(0)

            A2 = dot(*a,*a)
            B2 = dot(*b,*b)
            C  = dot(*a,*b)
            C2 = C*C

            u = a
            v = add(*mult(*b, A2), *mult(*a,-C))

            pu = dot(*p,*u) # == n1 * dot(u,u)
            pv = dot(*p,*v) # == n2 * dot(v,v)

            V2 = A2*(A2*B2-C2)

            V2_na = (A2*B2-C2)*pu - C*pv
            V2_nb = A2*pv

            if (V2_na % V2 == 0) and (V2_nb % V2 == 0):
                na,nb = V2_na//V2,V2_nb//V2
                score += costA * na + costB * nb

        print(score)
