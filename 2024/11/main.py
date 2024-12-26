from collections import Counter

def step():
    global rocks
    new_rocks = Counter()
    for value,count in rocks.items():
        if value == 0:
            new_rocks[1] += count
        elif (n := len(s := str(value))) % 2 == 0:
            new_rocks[int(s[:n//2])] += count
            new_rocks[int(s[n//2:])] += count
        else:
            new_rocks[value*2024] += count
    rocks = new_rocks

with open("input.txt") as file:
    rocks = Counter(int(i) for i in file.read().split())

    for i in range(25):
        step()
    print(rocks.total(),end=',')
    for i in range(50):
        step()
    print(rocks.total())
