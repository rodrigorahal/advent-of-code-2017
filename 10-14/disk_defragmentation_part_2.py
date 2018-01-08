from knot_hash_part_2 import get_hash_hex
from disk_defragmentation_part_1 import hash_to_bits

def get_rows(input):
    rows = []
    for i in range(128):
        hash_input = "{}-{}".format(input, i)
        hash_hex = get_hash_hex(hash_input)
        bits = hash_to_bits(hash_hex)
        rows.append(bits)
    return rows

def dfs(i, j, seen, rows):
    if ((i, j)) in seen:
        return

    if rows[i][j] == '0':
        return

    seen.add((i, j))

    if i > 0:
        dfs(i-1, j, seen, rows)
    if j > 0:
        dfs(i, j-1, seen, rows)
    if i < 127:
        dfs(i+1, j, seen, rows)
    if j < 127:
        dfs(i, j+1, seen, rows)

def find_groups(rows):
    ngroups = 0
    seen = set()

    for i in range(128):
        for j in range(128):
            if (i, j) in seen:
                continue
            if rows[i][j] == '0':
                continue
            ngroups += 1
            dfs(i, j, seen, rows)

    return ngroups

def main():
    test_case = 'flqrgnkx'
    assert find_groups(get_rows(test_case)) == 1242

    hash_input = 'ljoxqyyw'
    print('Answer: ', find_groups(get_rows(hash_input)))

if __name__ == '__main__':
    main()
