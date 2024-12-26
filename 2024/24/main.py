with open("input.txt") as file:
    wires, gates = file.read().split('\n\n')
    wires = {s[:3]: s[5]=='1' for s in wires.splitlines()}
    gates = {g[-3:]: (g[0:3],g[-10:-7],g[4:-11]) for g in gates.splitlines()}

    todo = dict(gates)
    while todo:
        for wire3 in dict(todo):
            wire1,wire2,op = gates[wire3]
            if wire1 in wires and wire2 in wires:
                del todo[wire3]
                match op:
                    case "AND": wires[wire3] = bool(wires[wire1] & wires[wire2])
                    case  "OR": wires[wire3] = bool(wires[wire1] | wires[wire2])
                    case "XOR": wires[wire3] = bool(wires[wire1] ^ wires[wire2])

    result = sorted(list((w,wires[w]) for w in wires if w[0] == 'z'))
    answer1 = sum((1 << i)*x for i,(_,x) in enumerate(result))

    wrong = set()
    for out,(in1,in2,op) in gates.items():
        usages = set(v[2] for v in gates.values() if out in v[:2])
        if in1[0] in "xy" and in1[1:] != '00':
            if op == 'XOR' and usages != set(['XOR','AND']):
                wrong.add(out)
            if op == 'AND' and usages != set(['OR']):
                wrong.add(out)
        elif (out[0] == 'z') ^ (op == 'XOR') and out != 'z45':
            wrong.add(out)

    answer2 = ','.join(sorted(wrong))
    print(answer1,answer2)

