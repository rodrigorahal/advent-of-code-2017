from input_stream import input_stream

def traverse_stream(stream):
    stream = (c for c in stream)
    stack = []
    scores = []

    for char in stream:

        if char == '<':
            while char != '>':
                char = next(stream)
                if char == '!':
                    next(stream)

        elif char == '{':
            stack.append(char)

        elif char == '}':
            group_score = len(stack)
            scores.append(group_score)
            stack.pop()

    return sum(scores)

def main():
    test_case_1 = '{}'
    assert traverse_stream(test_case_1) == 1

    test_case_2 = '{{{}}}'
    assert traverse_stream(test_case_2) == 6

    test_case_3 = '{{},{}}'
    assert traverse_stream(test_case_3) == 5

    test_case_4 = '{{{},{},{{}}}}'
    assert traverse_stream(test_case_4) == 16

    test_case_5 = '{<a>,<a>,<a>,<a>}'
    assert traverse_stream(test_case_5) == 1

    test_case_6 = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
    assert traverse_stream(test_case_6) == 9

    test_case_7 = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
    assert traverse_stream(test_case_7) == 9

    test_case_8 = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
    assert traverse_stream(test_case_8) == 3

    print('Answer: ', traverse_stream(input_stream))

if __name__ == '__main__':
    main()
