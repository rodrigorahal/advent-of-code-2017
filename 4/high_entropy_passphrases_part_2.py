from high_entropy_passphrases_part_1 import num_of_valid

def is_valid(passphrase):
    words = passphrase.split()
    sorted_words = [''.join(sorted(word)) for word in words]
    return len(sorted_words) == len(set(sorted_words))

def num_of_valid(passphrases):
    return sum(1 for passphrase in passphrases if is_valid(passphrase))

def main():
    with open('part_2_test_case.txt', 'r') as passphrases:
        assert num_of_valid(passphrases) == 3

    with open('input.txt', 'r') as passphrases:
        print("Answer: ", num_of_valid(passphrases))

if __name__ == '__main__':
    main()
