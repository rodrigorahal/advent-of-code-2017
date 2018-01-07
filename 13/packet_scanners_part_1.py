from itertools import cycle

def make_initial_state(rows):
    depths = dict()
    scanners = dict()

    for row in rows:
        l, d = row.split()

        layer = int(l.strip(':'))
        depth = int(d)

        depths[layer] = depth

        l1 = list(range(depth))
        l2 = list(reversed(l1[1:-1]))
        scanners[layer] = cycle(l1 + l2)

    return scanners, depths

def move_through_layers(scanners, depths):
    nlayers = max(scanners.keys())
    caught = []

    for packet_layer in range(nlayers+1):

        for scanner_layer, scanner_cycle in scanners.items():
            next_state = next(scanner_cycle)
            if packet_layer == scanner_layer:
                if next_state == 0:
                    caught.append((packet_layer, depths[packet_layer]))

    return caught

def severity(caught):
    prod = 0
    for l, d in caught:
        prod += l * d
    return prod

def main():
    with open('test_case.txt', 'r') as rows:
        scanners, depths = make_initial_state(rows)
        caught = move_through_layers(scanners, depths)
        assert severity(caught) == 24

    with open('input.txt', 'r') as rows:
        scanners, depths = make_initial_state(rows)
        caught = move_through_layers(scanners, depths)
        print('Answer: ', severity(caught))

if __name__ == '__main__':
    main()
