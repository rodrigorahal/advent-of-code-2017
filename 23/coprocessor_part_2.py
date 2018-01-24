"""
See input.txt
- if the program has exited, g had a value of 0 at line 29
- g == 0 at line 29 when b == c
- if g != 0 at line 29, b increments by 17
- b increments no other times on the program
- thus, lines 25 through 31 will run 1000 times,
  on values of b increasing by 17, before the program finishes.

- if f == 0 at line 25, h will increment by 1
- this can happen once and only once for any given value of b
- f == 0 if g == 0 at line 15
- g == 0 at line 15 if d * e == b
- since both d and e increment by 1 each in a loop,
  this will check every possible value of d and e less than b
- therefore, if b has any prime factors other than itself,
  f will be set to 1 at line 25.
"""

def assembly_bypass(initial):
    h = 0
    for b in range(initial, initial + 17000 + 1, 17):
        for g in range(2, b):
            if b % g == 0:
                h += 1
                break
    return h

def main():
    # initial values set at lines 1 to 6
    print('Answer: ', assembly_bypass(79 * 100 + 100000))

if __name__ == '__main__':
    main()
