from itertools import cycle, islice

def tie_knot(elements, pos, length, skip):
    size = len(elements)
    selected = []
    for i in range(pos, pos+length):
        if i < size:
            selected.append(elements[i])
        else:
            selected.append(elements[i-size])

    for i, el in zip(range(pos, pos+length), reversed(selected) ):
        if i < size:
            elements[i] = el
        else:
            elements[i-size] = el

    pos = pos + length + skip
    if pos >= size:
        pos -= size
    skip += 1

    return pos, skip

def knot_hash(elements, lengths):
    pos, skip = 0, 0

    for length in lengths:
        pos, skip = tie_knot(elements, pos, length, skip)

    return elements[0] * elements[1]

def main():
    part_1_test_case_elements = [0, 1, 2, 3, 4]
    part_1_test_case_lengths = [3, 4, 1, 5]
    assert knot_hash(part_1_test_case_elements, part_1_test_case_lengths) == 12

    elements = list(range(256))
    lengths = [189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62]
    print('Answer: ', knot_hash(elements, lengths))


if __name__ == '__main__':
    main()
