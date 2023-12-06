import re

with open('data.txt') as file:
    n_cards = [1] * 198
    n_left = 10
    answer1 = 0
    for ln, line in enumerate(file):
        numbers = list(re.findall(R"(\d+)", line))
        nums_left = set(numbers[1:n_left+1])
        nums_right = set(numbers[n_left+1:])
        n_matches = len(nums_left & nums_right)
        answer1 += 2 ** (n_matches-1) if n_matches else 0
        for i in range(n_matches):
            n_cards[ln+i+1] += n_cards[ln]

    answer2 = sum(n_cards)
    print(f"Part one: {answer1}")
    print(f"Part two: {answer2}")

    assert (answer1 == 21138)
    assert (answer2 == 7185540)
