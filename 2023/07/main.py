
sort_map1 = str.maketrans('TJQKA', 'ABCDE')
sort_map2 = str.maketrans('TJQKA', 'A0CDE')

HIGH_CARD, ONE_PAIR, TWO_PAIR, THREE_OF_A_KIND, FULL_HOUSE, FOUR_OF_A_KIND, FIVE_OF_A_KIND = range(
    7)

def value_hand(hand, jacks_wild):
    if (jacks_wild):
        wild = 'J'.translate(sort_map2)
        # NOTE- +[0] is needed if all cards are wild
        label_counts = [hand.count(h) for h in hand if h != wild] + [0]
        n_wilds = hand.count(wild)
    else:
        label_counts = [hand.count(h) for h in hand]
        n_wilds = 0
    if (5-n_wilds) in label_counts:
        return FIVE_OF_A_KIND
    elif (4-n_wilds) in label_counts:
        return FOUR_OF_A_KIND
    elif 3 in label_counts and 2 in label_counts:
        return FULL_HOUSE
    elif n_wilds > 0 and label_counts.count(2) > 2:
        return FULL_HOUSE
    elif (3-n_wilds) in label_counts:
        return THREE_OF_A_KIND
    elif label_counts.count(2) > 2:
        return TWO_PAIR
    elif (2-n_wilds) in label_counts:
        return ONE_PAIR
    else:
        return HIGH_CARD


def answer(jacks_wild):
    def parse(line):
        s = [sort_map1, sort_map2][jacks_wild]
        return line.translate(s).split()
    hs = sorted(map(parse, open("data.txt")))
    hs = sorted(hs, key=lambda x: value_hand(x[0], jacks_wild))

    values = ((i+1)*int(bet) for i, (_, bet) in enumerate(hs))
    return sum(values)


answer1 = answer(False)
answer2 = answer(True)

print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

assert (answer1 == 251136060)
assert (answer2 == 249400220)
