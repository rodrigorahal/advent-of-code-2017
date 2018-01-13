def dispatch_command(inst, registers):
    command, reg, value = inst

    try:
        value = int(value)
    except ValueError:
        value = int(registers[value])

    if command == 'set':
        registers[reg] = value

    if command == 'add':
        registers[reg] += value

    if command == 'mul':
        registers[reg] *= value

    if command == 'mod':
        registers[reg] = registers[reg] % value

    return registers


def dispatch(instructions, registers):
    sounds = []
    i = 0

    while True:
        inst = instructions[i].split()

        if len(inst) == 2:
            command, reg = inst

            if command == 'snd':
                sounds.append(registers[reg])

            elif command == 'rcv':
                if registers[reg] > 0:
                    return sounds[-1]

            i += 1

        else:
            command, reg, value = inst

            if command == 'jgz':
                if registers[reg] > 0:
                    i += int(value)
                else:
                    i +=1

            else:
                dispatch_command(inst, registers)
                i += 1

def initialize_registers(instructions):
    registers = {inst.split()[1]: 0 for inst in instructions}
    return registers

def main():
    with open('test_case.txt', 'r') as instructions:
        instructions = list(instructions)
        registers = initialize_registers(instructions)
        assert dispatch(instructions, registers) == 4

    with open('input.txt', 'r') as instructions:
        instructions = list(instructions)
        registers = initialize_registers(instructions)
        print(dispatch(instructions, registers))

if __name__ == '__main__':
    main()
