from dueling_generators_part_1 import compare_bins

def generator_a(start):
    prev = start
    while True:
        prev = (prev * 16807) % 2147483647
        if prev % 4 == 0:
            yield prev
        else:
            continue

def generator_b(start):
    prev = start
    while True:
        prev = (prev * 48271) % 2147483647
        if prev % 8 == 0:
            yield prev
        else:
            continue

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
    assert run_comparisons(a, b, n) == 0

    a, b, n = 65, 8921, 1056
    assert run_comparisons(a, b, n) == 1

    a, b, n = 65, 8921, 5 * pow(10, 6)
    assert run_comparisons(a, b, n) == 309

    a, b, n = 722, 354, 5 * pow(10, 6)
    print('Answer: ', run_comparisons(a, b, n))

if __name__ == '__main__':
    main()
