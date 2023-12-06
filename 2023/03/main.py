# ==================== Part 1 ====================
def get_value(line, index):
    if line[index].isdigit() and (index == 0 or not line[index-1].isdigit()):
        right_index = index+1
        while right_index < len(line) and line[right_index].isdigit():
            right_index += 1
        return right_index-1, int(line[index:right_index])
    else:
        return index, 0


def validate(lines, lno, cno_start, cno_end, _):
    l_start = max(lno-1, 0)
    l_end = min(lno+1, len(lines)-1)
    c_start = max(cno_start-1, 0)
    c_end = min(cno_end+1, len(lines[lno])-1)
    neighbours = [(y, x)
                  for y in range(l_start, l_end+1)
                  for x in range(c_start, c_end+1)]
    for d in neighbours:
        c = lines[d[0]][d[1]]
        if c != '.' and not c.isdigit():
            return True

    return False


# ==================== Part 2 ====================
def get_values(string, index):
    left_index = index - 1
    while left_index >= 0 and string[left_index].isdigit():
        left_index -= 1
    right_index = index + 1
    while right_index < len(string) and string[right_index].isdigit():
        right_index += 1

    if (string[index].isdigit()):
        ss = [string[left_index+1:right_index]]
    else:
        ss = [string[left_index+1:index], string[index+1:right_index]]
    return [int(s) for s in ss if s]


def get_touching_numbers(lines, line_no, char_no) -> list[int]:
    assert (lines[line_no][char_no] == '*')

    line_start = max(line_no-1, 0)
    line_end = min(line_no+1, len(lines)-1)
    ns = [n for line in lines[line_start: line_end+1]
          for n in get_values(line, char_no)
          if n]
    return ns


def calc_gear(values: list[int]):
    if len(values) == 2:
        return values[0] * values[1]
    else:
        return 0



with open('data.txt') as file:
    lines = file.read().strip().split('\n')

    numbers = ([(ln, cn, *vs)
                for ln, line in enumerate(lines)
                for cn, char in enumerate(line)
                if (vs := get_value(line, cn))[1]])
    answer = sum([p[3] for p in numbers if validate(lines, *p)])
    print(f"Part one: {answer}")

    gears = [calc_gear(get_touching_numbers(lines, ln, cn))
             for ln, line in enumerate(lines)
             for cn, char in enumerate(line)
             if char == '*']
    answer = sum(gears)
    print(f"Part two: {answer}")
