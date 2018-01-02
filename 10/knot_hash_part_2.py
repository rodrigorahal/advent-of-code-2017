from functools import reduce
from operator import xor

65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22

STANDARD_LENS_SUFFIX = [17, 31, 73, 47, 23]

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
    while pos >= size:
        pos -= size
    skip += 1

    return pos, skip

def run_round(elements, lengths, pos, skip):

    for length in lengths:
        pos, skip = tie_knot(elements, pos, length, skip)

    return pos, skip

def run_multiple_rounds(elements, lengths, nrounds=64):
    pos, skip = 0, 0
    for _ in range(nrounds):
        pos, skip = run_round(elements, lengths, pos, skip)
        # print(pos, skip)

    return elements

def get_dense_hash(elements):
    dense_hash = []
    for i in range(16):
        start = i * 16
        sub_hash = elements[start:start+16]
        reduced = reduce(xor, sub_hash)
        dense_hash.append(reduced)
    return dense_hash

def dense_hash_to_hex(dense_hash):
    return ''.join("{:02x}".format(el) for el in dense_hash)

def convert_lengths(input):

    lengths = [ord(char) for char in input]

    return lengths + STANDARD_LENS_SUFFIX

def main():
    elements = list(range(256))
    test_case_1 = ''
    lengths = convert_lengths(test_case_1)
    elements = run_multiple_rounds(elements, lengths)
    dense_hash = get_dense_hash(elements)
    hash_hex = dense_hash_to_hex(dense_hash)
    assert hash_hex == 'a2582a3a0e66e6e86e3812dcb672a272'

    elements = list(range(256))
    test_case_2 = 'AoC 2017'
    lengths = convert_lengths(test_case_2)
    elements = run_multiple_rounds(elements, lengths)
    dense_hash = get_dense_hash(elements)
    hash_hex = dense_hash_to_hex(dense_hash)
    assert hash_hex == '33efeb34ea91902bb2f59c9920caa6cd'

    elements = list(range(256))
    test_case_3 = '1,2,3'
    lengths = convert_lengths(test_case_3)
    elements = run_multiple_rounds(elements, lengths)
    dense_hash = get_dense_hash(elements)
    hash_hex = dense_hash_to_hex(dense_hash)
    assert hash_hex == '3efbe78a8d82f29979031a4aa0b16a9d'

    elements = list(range(256))
    test_case_4 = '1,2,4'
    lengths = convert_lengths(test_case_4)
    elements = run_multiple_rounds(elements, lengths)
    dense_hash = get_dense_hash(elements)
    hash_hex = dense_hash_to_hex(dense_hash)
    assert hash_hex == '63960835bcdc130f0b66d7ff4f6a5a8e'

    elements = list(range(256))
    input_lengths = '189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62'
    lengths = convert_lengths(input_lengths)
    elements = run_multiple_rounds(elements, lengths)
    dense_hash = get_dense_hash(elements)
    hash_hex = dense_hash_to_hex(dense_hash)
    print("Answer: ", hash_hex)


if __name__ == '__main__':
    main()
