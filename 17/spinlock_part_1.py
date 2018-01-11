
def next_insert(curr, nsteps, elements):
    size = len(elements)
    div, rem = divmod(nsteps, size)
    nxt = curr + rem + 1

    if nxt > size:
        while nxt > size:
            nxt -= size
    return nxt

def cycle(nsteps, limit=2017):
    elements = [0]
    curr = 0
    for value in range(1, limit+1):
        nxt_idx = next_insert(curr, nsteps, elements)
        elements.insert(nxt_idx, value)
        curr = nxt_idx
    return elements

def get_target(elements, target=2017):
    idx = elements.index(target)
    return elements[idx+1]

def main():
    test_case = 3
    elements = cycle(test_case, limit=2017)
    assert get_target(elements) == 638

    input = 356
    elements = cycle(input, limit=2017)
    print('Answer: ', get_target(elements))

if __name__ == '__main__':
    main()
