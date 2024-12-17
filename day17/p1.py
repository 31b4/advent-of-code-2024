def run_program(a, b, c, program):
    ip, output = 0, []
    reg = {'A': a, 'B': b, 'C': c}
    combo = lambda x: [0, 1, 2, 3, reg['A'], reg['B'], reg['C']][x]

    while ip < len(program):
        opcode, operand = program[ip], program[ip+1]
        if opcode == 0: reg['A'] //= 2**combo(operand)
        elif opcode == 1: reg['B'] ^= operand
        elif opcode == 2: reg['B'] = combo(operand) % 8
        elif opcode == 3: ip = operand if reg['A'] != 0 else ip + 2; continue
        elif opcode == 4: reg['B'] ^= reg['C']
        elif opcode == 5: output.append(str(combo(operand) % 8))
        elif opcode == 6: reg['B'] = reg['A'] // 2**combo(operand)
        elif opcode == 7: reg['C'] = reg['A'] // 2**combo(operand)
        ip += 2

    return ','.join(output)

with open("i.txt") as f:
    lines = f.read().splitlines()
    a = int(lines[0].split(": ")[1])
    b = int(lines[1].split(": ")[1])
    c = int(lines[2].split(": ")[1])
    program = list(map(int, lines[4].split(": ")[1].split(',')))

print(run_program(a, b, c, program))
