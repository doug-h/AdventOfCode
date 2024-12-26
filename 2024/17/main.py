import re

def combo(i):
    match i:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return regA
        case 5:
            return regB
        case 6:
            return regC
        case _:
            assert(0)


with open("input.txt") as file:
    regs, prog = file.read().split('\n\n')
    regA,regB,regC = [int(d) for d in re.findall(R" (\d+)", regs)]
    program = [int(d) for d in re.findall(R"(\d+)", prog)]
    ip = 0

    stdout = []

    while(ip < len(program)):
        opcode, operand = program[ip], program[ip+1]
        match opcode:
            case 0:
                #adv(operand)
                regA >>= combo(operand)
            case 1:
                #bxl(operand)
                regB ^= operand
            case 2:
                #bst(operand)
                regB = combo(operand) % 8
            case 3:
                #jnz(operand)
                if regA:
                    ip = operand-2
            case 4:
                #bxc(operand)
                regB ^= regC
            case 5:
                #out(operand)
                stdout.append(str(combo(operand) % 8))
            case 6:
                #bdv(operand)
                regB = regA >> combo(operand)
            case 7:
                #cdv(operand)
                regC = regA >> combo(operand)
        ip += 2
    print(",".join(stdout))
