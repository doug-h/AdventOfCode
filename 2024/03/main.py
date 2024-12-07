import re

with open('input.txt') as file:
    mem = "do()" + file.read() + "don't()"
    parts = [mem] + ["".join(re.findall(R"do\(\)([\S\s]*?)don't\(\)", mem))]
    mults = [re.findall(R"mul\((\d+),(\d+)\)", part) for part in parts]

    answer1, answer2 = [sum(int(a)*int(b) for a,b in line) for line in mults]

    print(answer1,answer2)

#188741603 67269798
