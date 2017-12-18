from registers_part_1 import check_conditional, initialize_registers

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
        new_value = operators[operator](registers[register], int(amount))
        registers[register] = new_value
        return new_value

def eval_instructions(instructions, registers):
    max_value = 0
    for inst in instructions:
        new_value = parse_and_eval_instruction(inst, registers)

        if new_value and new_value > max_value:
            max_value = new_value

    return registers, max_value

def main():
    with open('part_1_test_case.txt', 'r') as instructions:
        instructions = list(instructions)
        registers = initialize_registers(instructions)
        registers, max_value = eval_instructions(instructions, registers)
        assert max_value == 10

    with open('input.txt', 'r') as instructions:
        instructions = list(instructions)
        registers = initialize_registers(instructions)
        registers, max_value = eval_instructions(instructions, registers)
        print('Answer: ', max_value)


if __name__ == '__main__':
    main()
