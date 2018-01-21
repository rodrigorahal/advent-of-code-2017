def read_nodes(nodes_input):
    nodes = dict()

    for i, row in enumerate(nodes_input):
        for j, char in enumerate(row.strip()):
            nodes[(i, j)] = True if char == '#' else False

    return nodes

def get_initial_position(nodes):
    max_x = max(nodes.keys(), key=lambda p: p[0])[0]
    return max_x // 2, max_x // 2

def turn(direction, turn_direction):
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

def burst(position, direction, nodes, new_infected):
    infected = nodes.get(position, False)

    turn_direction = 'right' if infected else 'left'

    new_direction = turn(direction, turn_direction)

    if infected:
        # clean node
        nodes[position] = False
    else:
        # infect node
        nodes[position] = True
        new_infected.append(position)

    nodes[position] = False if infected else True

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
        nodes, new_infected = run_infection(initial_position, nodes, n=10000)
        assert len(new_infected) == 5587

    with open('input.txt') as nodes_input:
        nodes = read_nodes(nodes_input)
        initial_position = get_initial_position(nodes)
        nodes, new_infected = run_infection(initial_position, nodes, n=10000)
        print('Answer: ', len(new_infected))

if __name__ == '__main__':
    main()
