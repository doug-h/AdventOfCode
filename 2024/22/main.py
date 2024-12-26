import itertools

def step(secret_number):
    secret_number ^= (secret_number << 6)
    secret_number &= ((1 << 24)-1)
    secret_number ^= (secret_number >> 5)
    secret_number &= ((1 << 24)-1)
    secret_number ^= (secret_number << 11)
    secret_number &= ((1 << 24)-1)
    return secret_number

def step_n(secret_number, n):
    for _ in range(n):
        secret_number = step(secret_number)
    return secret_number


with open("input.txt") as file:
    numbers = list(map(int,file.read().splitlines()))
    answer1 = sum(step_n(i,2000) for i in numbers)
    deltas = []
    prices = []
    for n in numbers:
        dn = []
        pn = [n%10]
        x = n
        for _ in range(2000):
            s = step(x)
            pn.append(s%10)
            dn.append(s%10-x%10)
            x = s
        deltas.append(list(dn))
        prices.append(list(pn))

    amounts = []
    for dn,pn in zip(deltas,prices):
        scores = {}
        for i in range(len(dn)-3):
            key = tuple(dn[i:i+4])
            if key not in scores:
                scores[key] = pn[i+4]
        amounts.append(dict(scores))

    answer2 = 0
    best_delta = (0,0,0,0)
    for key in itertools.product(range(-9,10),repeat=4):
        price = 0
        for scores in amounts:
            if key in scores:
                price += scores[key]
        if price > answer2:
            answer2 = price
            best_delta = key
            print(key)
    print(answer1,answer2)
