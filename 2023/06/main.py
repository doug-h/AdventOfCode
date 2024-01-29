import math 


# ==================== Part one ====================
with open("data.txt") as file:
    times,distances = [[int(x) for x in line.split()[1:]]
             for line in file.read().split('\n')[:-1]]
    counts = [len(list(s for s in range(t) if s*(t-s)>d)) for t,d in zip(times,distances)]
    answer1= math.prod(counts)


# ==================== Part two ====================
with open("data.txt") as file:
    t,d = [int(x) for line in file.read().split('\n')[:-1]
                for x in [line[9:].replace(" ", "")]]

    q= math.sqrt(t*t-4*d)
    # NOTE - if q is an int then just doing floor/ceil 
    #   would give the wrong answer, that's why I do 
    #   ceil(X-1)/floor(X+1)
    upper_limit = math.ceil((t+q)/2-1)
    lower_limit = math.floor((t-q)/2+1)
    answer2 = upper_limit-lower_limit+1

             
    print(f"Part one: {answer1}")
    print(f"Part two: {answer2}")




