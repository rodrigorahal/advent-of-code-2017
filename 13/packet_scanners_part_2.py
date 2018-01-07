from copy import deepcopy
from itertools import cycle, count

from packet_scanners_part_1 import make_initial_state

def scanner_depth(depth, time):
    '''Returns scanner's depth position in the given time'''
    offset = time % ((depth - 1) * 2)

    return 2 * (depth - 1) - offset if offset > depth - 1 else offset

def find_delay(depths):
    for wait in count():
        scanners = []
        for layer in depths:
            scanners.append(scanner_depth(depths[layer], wait + layer))
        if not any(s == 0 for s in scanners):
            return wait

def main():
    with open('test_case.txt', 'r') as rows:
        scanners, depths = make_initial_state(rows)
        assert find_delay(depths) == 10

    with open('input.txt', 'r') as rows:
        scanners, depths = make_initial_state(rows)
        print('Answer: ', find_delay(depths))

if __name__ == '__main__':
    main()
