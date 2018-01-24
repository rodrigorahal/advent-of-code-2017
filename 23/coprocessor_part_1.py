import string

def dispatch_command(inst, registers):
    command, reg, value = inst

    try:
        value = int(value)
    except ValueError:
        value = int(registers[value])

    if command == 'set':
        registers[reg] = value

    if command == 'sub':
        registers[reg] -= value

    if command == 'mul':
        registers[reg] *= value

    return registers

def dispatch(instructions, registers):
    i = 0
    nmul = 0

    while True:
        if i >= len(instructions):
            return nmul


        inst = instructions[i].split()

        command, reg, value = inst

        if command == 'jnz':
            try:
                reg_value = int(reg)
            except ValueError:
                reg_value = registers[reg]

            if reg_value != 0:
                i += int(value)
            else:
                i +=1

        else:
            dispatch_command(inst, registers)
            i += 1
            if command == 'mul':
                nmul += 1

def initialize_registers():
    registers = {letter: 0 for letter in string.ascii_lowercase}
    return registers

def main():
    with open('input.txt') as instructions:
        instructions = list(instructions)
        registers = initialize_registers()
        print('Answer: ', dispatch(instructions, registers))

if __name__ == '__main__':
    main()
