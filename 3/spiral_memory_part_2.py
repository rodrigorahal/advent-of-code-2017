from spiral_memory_part_1 import moves

def sum_adjacents(position, position_to_number):
    x_p, y_p = position
    adjacents = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            n = position_to_number.get((x_p + x, y_p + y), 0)
            adjacents.append(n)
    return sum(adjacents)


def spiral_position(number):
    n = 1
    position = (0, 0)
    times_to_move = 1

    position_to_number = {position: n}

    while True:
        for _ in range(2):
            move = next(moves)
            for _ in range(times_to_move):
                if n >= number:
                    return n
                position = move(*position)
                n = sum_adjacents(position, position_to_number)
                position_to_number[position] = n
        times_to_move += 1

def main():

    print("Answer: ", spiral_position(277678))

if __name__ == '__main__':
    main()
