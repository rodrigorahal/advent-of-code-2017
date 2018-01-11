from spinlock_part_1 import next_insert

def next_insert(curr, nsteps, size):
    div, rem = divmod(nsteps, size)
    nxt = curr + rem + 1

    if nxt > size:
        while nxt > size:
            nxt -= size
    return nxt

def cycle(nsteps, limit=2017):
    curr = 0
    target_id = 1
    target = None

    for value in range(1, limit+1):

        nxt_idx = next_insert(curr, nsteps, value)

        if nxt_idx == 0:
            target_id += 1

        if nxt_idx == target_id:
            target = value

        curr = nxt_idx

    return target

def main():
    input = 356
    target = cycle(input, limit=50000000)
    print('Answer: ', target)

if __name__ == '__main__':
    main()
