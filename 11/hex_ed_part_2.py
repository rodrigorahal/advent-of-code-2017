from hex_ed_part_1 import moves_cube_coord, next_position

def pos_to_distance(pos):
    x, y, z = pos

    return (abs(x) + abs(y) + abs(z)) // 2

def hex_distance(moves):
    pos = 0, 0, 0
    furthest = 0

    for move in moves:
        pos = next_position(pos, move)
        dist = pos_to_distance(pos)

        if dist > furthest:
            furthest = dist

    return furthest

def main():
    with open('input.txt', 'r') as f:
        moves = next(f)
        moves = moves.rstrip('\n').split(',')
        print('Answer: ', hex_distance(moves))

if __name__ == '__main__':
    main()
