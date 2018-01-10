import string

def make_move(instruction, elements):
    move = instruction[0]

    if move == 's':
        return spin(elements, int(instruction[1:]))

    if move == 'x':
        a, b = instruction[1:].split('/')
        return exchange(elements, int(a), int(b))

    if move == 'p':
        a, b = instruction[1:].split('/')
        return partner(elements, a, b)

def spin(elements, n):
    return elements[-n:] + elements[:len(elements)-n]

def exchange(elements, a, b):
    elements[a], elements[b] = elements[b], elements[a]
    return elements

def partner(elements, a, b):
    ia = elements.index(a)
    ib = elements.index(b)
    return exchange(elements, ia, ib)

def dance(elements, instructions):

    for instruction in instructions:
        elements = make_move(instruction, elements)

    return ''.join(elements)


def main():
    elements = list(string.ascii_lowercase[:5])
    instructions = ['s1', 'x3/4', 'pe/b']
    assert dance(elements, instructions) == 'baedc'

    with open('input.txt') as f:
        elements = list(string.ascii_lowercase[:16])
        for line in f:
            instructions = list(line.split(','))
            print('Answer: ', dance(elements, instructions))


if __name__ == '__main__':
    main()
