from knot_hash_part_2 import get_hash_hex

def count_used_squares(input):
    count = 0
    for i in range(128):
        hash_input = "{}-{}".format(input, i)
        hash_hex = get_hash_hex(hash_input)
        bits = hash_to_bits(hash_hex)
        count += bits.count('1')
    return count

def hash_to_bits(hash_hex):
    state = ''
    for char in hash_hex:
        state += bin(int(char, 16))[2:].zfill(4)
    return state

def main():
    test_case = 'flqrgnkx'
    assert count_used_squares(test_case) == 8108

    hash_input = 'ljoxqyyw'
    print(count_used_squares(hash_input))

if __name__ == '__main__':
    main()
