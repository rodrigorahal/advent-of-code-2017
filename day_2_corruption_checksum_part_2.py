
def checksum(spreasheet):
    divs = []
    for row in spreasheet:
        numbers = sorted(int(num) for num in row.split())
        for i, num in enumerate(numbers):
            for j in range(i+1, len(numbers)):
                if numbers[j] % num == 0:
                    divs.append(numbers[j] / num)
    return int(sum(divs))


def main():
    with open('corruption_checksum_part_2_test_case.txt', 'r') as spreasheet:
        assert checksum(spreasheet) == 9

    with open('corruption_checksum.txt', 'r') as spreasheet:
        print("Answer: ", checksum(spreasheet))

if __name__ == '__main__':
    main()
