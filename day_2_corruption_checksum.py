
def row_min_max(row):
    nums = row.split()
    smallest = min(int(num) for num in nums)
    largest = max(int(num) for num in nums)

    return smallest, largest

def checksum(spreasheet):
    diffs = []
    for row in spreasheet:
        smallest, largest = row_min_max(row)
        diffs.append(largest - smallest)

    return sum(diffs)

def main():
    with open('corruption_checksum_test_case.txt', 'r') as spreasheet:
        assert checksum(spreasheet) == 18

    with open('corruption_checksum.txt', 'r') as spreasheet:
        print("Answer: ", checksum(spreasheet))

if __name__ == '__main__':
    main()
