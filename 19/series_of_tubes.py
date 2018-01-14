import string

letters = set(string.ascii_uppercase)

directions = {
    'down': (1, 0),
    'up': (-1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

def make_grid(diagram):
    grid = []
    for i, row in enumerate(diagram):
        moves = []
        for m in row.strip('\n'):
            moves.append(m)
        grid.append(moves)
    return grid


def find_start(grid):
    for j, char in enumerate(grid[0]):
        if char == '|':
            return 0, j, 'down'

def navigate(grid, start):
    path = []
    i, j, direction = start

    steps = 0
    while direction != 'end':
        i, j, direction = next_pos(grid, (i, j), direction, path)
        steps += 1

    print('steps: ', steps-1)
    return ''.join(path)


def next_pos(grid, curr, direction, path):
    i, j = curr
    try:
        move = grid[i][j]
    except IndexError:
        return i,j, 'end'

    if move == ' ' or i < 0 or j < 0:
        return i, j, 'end'

    if move == '+':
        if direction in ('down', 'up'):
            if grid[i][j+1] != ' ':
                return i, j+1, 'right'
            else:
                return i, j-1, 'left'

        if direction in ('right', 'left'):
            if grid[i+1][j] != ' ':
                return i+1, j, 'down'
            else:
                return i-1, j, 'up'

    if move in letters:
        path.append(move)

    i_inc, j_inc = directions[direction]
    return i + i_inc, j + j_inc, direction

def main():
    with open('input.txt', 'r') as diagram:
        grid = make_grid(diagram)
        start = find_start(grid)
        print('Answer: ', navigate(grid, start))

if __name__ == '__main__':
    main()
