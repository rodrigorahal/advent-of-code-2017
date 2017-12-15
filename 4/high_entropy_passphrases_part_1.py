
def is_valid(passphrase):
    words = passphrase.split()
    return len(words) == len(set(words))

def num_of_valid(passphrases):
    return sum(1 for passphrase in passphrases if is_valid(passphrase))

def main():
    with open('part_1_test_case.txt', 'r') as passphrases:
        assert num_of_valid(passphrases) == 2

    with open('input.txt', 'r') as passphrases:
        print("Answer: ", num_of_valid(passphrases))

if __name__ == '__main__':
    main()
