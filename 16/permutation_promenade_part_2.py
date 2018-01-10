import string
import copy
from permutation_promenade_part_1 import dance

def dance_pattern(prev, next):
    pos = {}
    for i, prev_pos in enumerate(prev):
        next_pos = next.index(prev_pos)
        pos[i] = next_pos
    return pos

def run_dance(elements, instructions, n):
    elements = list(elements)
    prev = copy.deepcopy(elements)
    for _ in range(n):
        elements = dance(elements, instructions)
        elements = list(elements)
    return list(prev), list(elements)

def simulate_dance(elements, pattern):
    modified = [None for _ in range(len(elements))]

    for i, el in enumerate(elements):
        to = pattern[i]
        modified[to] = el

    return modified

def keep_dancing(elements, pattern, n):
    for _ in range(n):
        elements = simulate_dance(elements, pattern)
    return ''.join(elements)

def main():
    with open('input.txt') as f:
        elements = list(string.ascii_lowercase[:16])
        for line in f:
            instructions = list(line.split(','))
            prev, next = run_dance(copy.deepcopy(elements), instructions, 1000)
            pattern = dance_pattern(prev, next)
            print('Answer: ', keep_dancing(elements, pattern, pow(10, 6)))


if __name__ == '__main__':
    main()
