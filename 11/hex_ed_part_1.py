moves_cube_coord = {
    'ne': (1, 0, -1),
    'n':  (0, 1, -1),
    'nw': (-1, 1, 0),
    'sw': (-1, 0, 1),
    's':  (0, -1, 1),
    'se': (1, -1, 0),
}

def next_position(pos, move):
    dx, dy, dz = moves_cube_coord[move]
    x, y, z = pos
    return x + dx, y + dy, z + dz

def hex_distance(moves):
    pos = 0, 0, 0

    for move in moves:
        pos = next_position(pos, move)

    x, y, z = pos

    return (abs(x) + abs(y) + abs(z)) // 2

def main():
    test_case_1 = ['ne', 'ne', 'ne']
    assert hex_distance(test_case_1) == 3

    test_case_2 = ['ne', 'ne', 'sw', 'sw']
    assert hex_distance(test_case_2) == 0

    test_case_3 = ['ne', 'ne', 's', 's']
    assert hex_distance(test_case_3) == 2

    test_case_4 = ['se', 'sw', 'se', 'sw', 'sw']
    assert hex_distance(test_case_4) == 3

    with open('input.txt', 'r') as f:
        moves = next(f)
        moves = moves.rstrip('\n').split(',')
        print('Answer: ', hex_distance(moves))

if __name__ == '__main__':
    main()
