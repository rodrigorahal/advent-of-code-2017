def read_nodes(nodes_input):
    nodes = dict()

    for i, row in enumerate(nodes_input):
        for j, char in enumerate(row.strip()):
            nodes[(i, j)] = 'I' if char == '#' else 'C'

    return nodes

def get_initial_position(nodes):
    max_x = max(nodes.keys(), key=lambda p: p[0])[0]
    return max_x // 2, max_x // 2

def turn(direction, turn_direction):
    if turn_direction == 'current':
        return direction

    if turn_direction == 'right':
        if direction == 'up':
            return 'right'
        if direction == 'right':
            return 'down'
        if direction == 'down':
            return 'left'
        if direction == 'left':
            return 'up'

    if turn_direction == 'left':
        if direction == 'up':
            return 'left'
        if direction == 'right':
            return 'up'
        if direction == 'down':
            return 'right'
        if direction == 'left':
            return 'down'

    if turn_direction == 'reverse':
        if direction == 'up':
            return 'down'
        if direction == 'right':
            return 'left'
        if direction == 'down':
            return 'up'
        if direction == 'left':
            return 'right'

def next_position(position, direction):
    x, y = position

    if direction == 'left':
        return x, y - 1

    if direction == 'right':
        return x, y + 1

    if direction == 'up':
        return x - 1, y

    if direction == 'down':
        return x + 1, y

def get_next_state(position, nodes):
    state = nodes.get(position, 'C')

    if state == 'C':
        next_state = 'W'
    if state == 'W':
        next_state = 'I'
    if state == 'I':
        next_state = 'F'
    if state == 'F':
        next_state = 'C'

    return next_state

def get_turn_direction(position, nodes):
    state = nodes.get(position, 'C')

    if state == 'C':
        turn_direction = 'left'

    if state == 'W':
        turn_direction = 'current'

    if state == 'I':
        turn_direction = 'right'

    if state == 'F':
        turn_direction = 'reverse'

    return turn_direction

def burst(position, direction, nodes, new_infected):
    turn_direction = get_turn_direction(position, nodes)

    new_direction = turn(direction, turn_direction)

    next_state = get_next_state(position, nodes)

    nodes[position] = next_state

    if next_state == 'I':
        new_infected.append(position)

    next_pos = next_position(position, new_direction)

    return next_pos, new_direction

def run_infection(position, nodes, direction='up', n=70):
    new_infected = []

    for i in range(n):
        position, direction = burst(position, direction, nodes, new_infected)

    return nodes, new_infected

def main():
    with open('test_case.txt') as nodes_input:
        nodes = read_nodes(nodes_input)
        initial_position = get_initial_position(nodes)
        nodes, new_infected = run_infection(initial_position, nodes, n=100)
        assert len(new_infected) == 26

    with open('input.txt') as nodes_input:
        nodes = read_nodes(nodes_input)
        initial_position = get_initial_position(nodes)
        nodes, new_infected = run_infection(initial_position, nodes, n=10000000)
        print('Answer: ', len(new_infected))

if __name__ == '__main__':
    main()
