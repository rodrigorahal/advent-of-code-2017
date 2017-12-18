from itertools import cycle

def reallocate_memory(state):
    max_id, max_blocks = 0, state[0]
    for idx, nblocks in enumerate(state):
        if nblocks > max_blocks:
            max_id = idx
            max_blocks = nblocks

    state[max_id] = 0
    ids = cycle(range(len(state)))

    idx = next(ids)
    while idx != max_id:
        idx = next(ids)

    while max_blocks:
        idx = next(ids)
        state[idx] += 1
        max_blocks -= 1

    return state

def reallocation_cycles(state):
    seen_states = set()
    seen_states.add(tuple(state))

    while True:
        next_state = reallocate_memory(state)

        if tuple(next_state) in seen_states:
            return len(seen_states)

        seen_states.add(tuple(next_state))

def main():
    test_case = [0, 2, 7, 0]

    assert reallocation_cycles(test_case) == 5

    input_state = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]

    print("Answer: ", reallocation_cycles(input_state))

if __name__ == '__main__':
    main()
