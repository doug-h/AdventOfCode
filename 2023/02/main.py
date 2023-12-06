import re
import math

with open('data.txt') as file:
    allowed_counts = {"red": 12, "green": 13, "blue": 14}

    answer1 = 0
    answer2 = 0
    for ln, line in enumerate(file):
        min_counts = {"red": 0, "green": 0, "blue": 0}
        for count, colour in re.findall(R"(\d+) (\w+)", line):
            min_counts[colour] = max(int(count), min_counts[colour])
        answer1 += (ln+1) * all(min_counts[c] <= allowed
                               for c, allowed in allowed_counts.items())
        answer2 += math.prod(min_counts.values())
    print(f"Part one: {answer1}")
    print(f"Part two: {answer2}")
