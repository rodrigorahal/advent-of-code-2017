import ipdb
import copy
from duet_part_1 import dispatch_command

def initialize_registers(instructions):
    registers_0 = dict()

    for inst in instructions:
        reg = inst.split()[1]

        try:
            int(reg)
        except ValueError:
            registers_0[reg] = 0

    registers_1 = copy.deepcopy(registers_0)
    registers_1['p'] = 1

    return registers_0, registers_1


def dispatch(instructions, registers, snd_msq, rcv_msq, recorded, record=False):
    i = 0

    while True:
        if i == len(instructions):
            yield i

        inst = instructions[i].split()

        if len(inst) == 2:
            command, reg = inst

            try:
                reg_value = int(reg)
            except ValueError:
                reg_value = registers[reg]

            if command == 'snd':
                snd_msq.append(reg_value)
                i += 1

                if record:
                    recorded.append(reg_value)

            elif command == 'rcv':
                if rcv_msq:
                    registers[reg] = rcv_msq.pop(0)
                    i += 1
                else:
                    yield i

        else:
            command, reg, value = inst

            if command == 'jgz':

                try:
                    value = int(value)
                except ValueError:
                    value = registers[value]

                try:
                    reg_value = int(reg)
                except ValueError:
                    reg_value = registers[reg]

                if reg_value > 0:
                    i += int(value)
                else:
                    i +=1

            else:
                dispatch_command(inst, registers)
                i += 1

def run_parallel(registers_0, registers_1, instructions):
    msq_0 = []
    msq_1 = []
    sent_by_1 = []

    end = len(instructions)

    program_0 = dispatch(instructions, registers_0, msq_1, msq_0, sent_by_1,
                         record=False)
    program_1 = dispatch(instructions, registers_1, msq_0, msq_1, sent_by_1,
                         record=True)

    i_0, i_1 = 0, 0

    while True:
        if i_0 < end:
            i_0 = next(program_0)


        if i_1 < end:
            i_0 = next(program_1)

        if (not msq_0 and not msq_1) or (i_0 == end and i_1 == end):
            return len(sent_by_1)

def main():
    with open('test_case_2.txt', 'r') as instructions:
        instructions = list(instructions)
        registers_0, registers_1 = initialize_registers(instructions)
        assert run_parallel(registers_0, registers_1, instructions) == 3

    with open('input.txt', 'r') as instructions:
        instructions = list(instructions)
        registers_0, registers_1 = initialize_registers(instructions)
        print(run_parallel(registers_0, registers_1, instructions))

if __name__ == '__main__':
    main()
