with open('input.txt') as file:
    differences = lambda l : [b-a for a,b in zip(l[:-1], l[1:])]
    valid_rule = lambda rule :(all(abs(d) >= 1 and abs(d) <= 3 for d in rule) and 
                              (all(d > 0 for d in rule) or all(d < 0 for d in rule)))

    rules = [[int(i) for i in line.split()] for line in file]
    diffs = map(differences, rules)

    answer1 = sum(1 for d in diffs if valid_rule(d))

    perms = ([r] + [r[:i] + r[i+1:] for i in range(len(r))] for r in rules)
    diffs = ((differences(perm) for perm in rule) for rule in perms)
    answer2 = sum(1 for d in diffs if any(valid_rule(p) for p in d))


    print(answer1)
    print(answer2)
    #287
    #354
