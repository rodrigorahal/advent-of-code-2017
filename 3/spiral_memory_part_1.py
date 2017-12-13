from itertools import cycle

def move_right(x, y):
    return x + 1, y

def move_up(x, y):
    return x, y + 1

def move_left(x, y):
    return x - 1, y

def move_down(x, y):
    return x, y - 1

moves = cycle([move_right, move_up, move_left, move_down])

def spiral_position(number):
    n = 1
    position = (0, 0)
    times_to_move = 1

    while True:
        for _ in range(2):
            move = next(moves)
            for _ in range(times_to_move):
                if n >= number:
                    return position
                position = move(*position)
                n += 1
        times_to_move += 1

def count_steps(position):
    x, y = position
    return abs(x) + abs(y)

def main():
    assert count_steps(spiral_position(1)) == 0

    assert count_steps(spiral_position(12)) == 3

    assert count_steps(spiral_position(23)) == 2

    assert count_steps(spiral_position(1024)) == 31

    print("Answer: ", count_steps(spiral_position(277678)))

if __name__ == '__main__':
    main()
