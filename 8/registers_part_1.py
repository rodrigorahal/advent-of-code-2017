import operator

operators = {
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt,
    'inc': operator.add,
    'dec': operator.sub,
}

def parse_and_eval_instruction(instruction, registers):
    """n dec 271 if az < 3"""
    register, operator, amount, _, cond_register, cond_operator, cond_operand = instruction.split()
    if check_conditional(cond_register, cond_operator, cond_operand, registers):
        registers[register] = operators[operator](registers[register], int(amount))

def check_conditional(cond_register, cond_operator, cond_operand, registers):
    return operators[cond_operator](registers[cond_register], int(cond_operand))

def initialize_registers(instructions):
    registers = dict()

    for inst in instructions:
        register = inst.split()[0]
        cond_register = inst.split()[4]

        registers[register] = 0
        registers[cond_register] = 0

    return registers

def eval_instructions(instructions, registers):
    for inst in instructions:
        parse_and_eval_instruction(inst, registers)

    return registers

def find_max_stored_value(registers):
    return max(registers.values())

def main():
    with open('part_1_test_case.txt', 'r') as instructions:
        instructions = list(instructions)
        registers = initialize_registers(instructions)
        registers = eval_instructions(instructions, registers)
        assert find_max_stored_value(registers) == 1

    with open('input.txt', 'r') as instructions:
        instructions = list(instructions)
        registers = initialize_registers(instructions)
        registers = eval_instructions(instructions, registers)
        print('Answer: ', find_max_stored_value(registers))


if __name__ == '__main__':
    main()
