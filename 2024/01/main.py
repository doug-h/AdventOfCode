with open('input.txt') as file:
    ids = [map(int, line.split()) for line in file]
    col1, col2 = zip(*ids)

    answer1 = sum(abs(b-a) for a,b in zip(sorted(col1), sorted(col2)))
    answer2 = sum(a for a in col2 if a in set(col1))

print(answer1)
print(answer2)

#2113135
#19097157
