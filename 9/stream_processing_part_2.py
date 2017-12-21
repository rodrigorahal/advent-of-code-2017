from input_stream import input_stream

def traverse_stream(stream):
    stream = (c for c in stream)
    stack = []
    scores = []
    garbage = []

    for char in stream:

        if char == '<':
            while char != '>':
                char = next(stream)
                if char == '!':
                    next(stream)
                elif char != '>':
                    garbage.append(char)

        elif char == '{':
            stack.append(char)

        elif char == '}':
            group_score = len(stack)
            scores.append(group_score)
            stack.pop()

    return len(garbage)

def main():
    test_case_1 = '<>'
    assert traverse_stream(test_case_1) == 0

    test_case_2 = '<random characters>'
    assert traverse_stream(test_case_2) == 17

    test_case_3 = '<<<<>'
    assert traverse_stream(test_case_3) == 3

    test_case_4 = '<{!>}>'
    assert traverse_stream(test_case_4)  == 2

    test_case_5 = '<!!>'
    assert traverse_stream(test_case_5) == 0

    test_case_6 = '<!!!>>'
    assert traverse_stream(test_case_6) == 0

    test_case_7 = '<{o"i!a,<{i<a>'
    assert traverse_stream(test_case_7) == 10

    print('Answer: ', traverse_stream(input_stream))

if __name__ == '__main__':
    main()
