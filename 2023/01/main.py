digit_names = ['one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']


def is_digitname(line):
    if (len(line) < 3):
        return 0

    for i, name in enumerate(digit_names):
        if ((len(name) <= len(line))
                and (line[:len(name)] == name)):

            return i+1
    return 0


def process_line(line: str) -> int:
    value = 0
    for i in range(len(line)):
        if (c := line[i]).isdigit():
            value = 10*int(c)
            break
        idx = is_digitname(line[i:])
        if (idx):
            value = 10*idx
            break

    for i in range(len(line)-1, -1, -1):
        if (c := line[i]).isdigit():
            value += int(c)
            break
        idx = is_digitname(line[i:])
        if (idx):
            value += idx
            break
    return value


with open('data.txt') as file:
    value = sum([process_line(l) for l in file])
    print(value)
