
def walk_maze(maze):
    num_steps = 0
    i = 0

    while True:
        try:
            jump_inc = maze[i]
            maze[i] += 1
            num_steps += 1
            i += jump_inc
        except IndexError:
            return num_steps

def main():
    with open('part_1_test_case.txt', 'r') as f:
        maze = [int(row.split()[0]) for row in f]
        assert walk_maze(maze) == 5

    with open('input.txt', 'r') as f:
        maze = [int(row.split()[0]) for row in f]
        print("Answer: ", walk_maze(maze))

if __name__ == '__main__':
    main()
