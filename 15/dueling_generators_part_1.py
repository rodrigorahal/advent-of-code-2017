

def generator_a(start):
    prev = start
    while True:
        prev = (prev * 16807) % 2147483647
        yield prev

def generator_b(start):
    prev = start
    while True:
        prev = (prev * 48271) % 2147483647
        yield prev

def compare_bins(a, b):
    return bin(a)[2:].zfill(32)[-16:] == bin(b)[2:].zfill(32)[-16:]

def run_comparisons(start_a, start_b, n):
    gen_a = generator_a(start_a)
    gen_b = generator_b(start_b)

    equals = 0

    for _ in range(n):
        if compare_bins(next(gen_a), next(gen_b)):
            equals += 1

    return equals

def main():
    a, b, n = 65, 8921, 6
    assert run_comparisons(a, b, n) == 1

    a, b, n = 65, 8921, 40 * pow(10, 6)
    assert run_comparisons(a, b, n) == 588

    a, b, n = 722, 354, 40 * pow(10, 6)
    print('Answer: ', run_comparisons(a, b, n))

if __name__ == '__main__':
    main()
