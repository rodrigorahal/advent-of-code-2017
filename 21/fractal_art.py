import numpy as np

def read_rules(rules_input):
    rules = {}

    for line in rules_input:
        patt, out = line.strip().split(' => ')

        patt = np.array([[p == '#' for p in row] for row in patt.split('/')], dtype=bool)
        out = np.array([[p == '#' for p in row] for row in out.split('/')], dtype=bool)

        add_variations(patt, out, rules)

    return rules

def add_variations(pattern, output, rules):
    patt = pattern
    flip = np.flip(patt, axis=1)

    for _ in range(4):
        rules[patt.tobytes()] = output
        rules[flip.tobytes()] = output
        patt, flip = np.rot90(patt), np.rot90(flip)

    return rules

def enhance(grid, rules):
    size = len(grid)
    by = 2 if size % 2 == 0 else 3

    new_size = size * (by + 1) // by

    enhanced = np.empty((new_size, new_size), dtype=bool)

    squares = list(range(0, size, by))
    new_squares = list(range(0, new_size, by+1))

    for i, ni in zip(squares, new_squares):
        for j, nj in zip(squares, new_squares):
            pattern = grid[i:i+by, j:j+by]
            rule = rules[pattern.tobytes()]
            enhanced[ni:ni+by+1, nj:nj+by+1] = rule

    return enhanced

def run_enhance(rules, grid=None, n=5):
    if not grid:
        grid = np.array([
            [False, True, False],
            [False, False, True],
            [True, True, True]
        ])

    for i in range(n):
        grid = enhance(grid, rules)

    return grid

def count_pixels(grid):
    return int(grid.sum())

def main():
    with open('test_case.txt', 'r') as rules_input:
        rules = read_rules(rules_input)
        grid = run_enhance(rules, n=2)
        assert count_pixels(grid) == 12

    with open('input.txt', 'r') as rules_input:
        rules = read_rules(rules_input)
        grid = run_enhance(rules, n=5)
        print('Answer: ', count_pixels(grid))

    with open('input.txt', 'r') as rules_input:
        rules = read_rules(rules_input)
        grid = run_enhance(rules, n=18)
        print('Answer: ', count_pixels(grid))

if __name__ == '__main__':
    main()
