instructions = {
    ('A', 0): (1, +1, 'B'),
    ('A', 1): (0, -1, 'D'),

    ('B', 0): (1, +1, 'C'),
    ('B', 1): (0, +1, 'F'),

    ('C', 0): (1, -1, 'C'),
    ('C', 1): (1, -1, 'A'),

    ('D', 0): (0, -1, 'E'),
    ('D', 1): (1, +1, 'A'),

    ('E', 0): (1, -1, 'A'),
    ('E', 1): (0, +1, 'B'),

    ('F', 0): (0, +1, 'C'),
    ('F', 1): (0, +1, 'E'),
}

def step(i, state, values, instructions):
    value = values.get(i, 0)

    write, direc, next_state = instructions[(state, value)]

    values[i] = write

    return i + direc, next_state

def machine(instructions, n=12302209):
    i = 0
    state = 'A'
    tape = {}

    for _ in range(n):
        i, state = step(i, state, tape, instructions)

    return sum(tape.values())

def main():
    print(machine(instructions))

if __name__ == '__main__':
    main()
