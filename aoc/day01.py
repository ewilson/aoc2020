from aoc.util import puzzle_input


def compute1():
    input_nums = puzzle_input(__file__, int)
    pair = next(((n1, n2) for i1, n1 in enumerate(input_nums) for i2, n2 in enumerate(input_nums) if i1 < i2 and n1 + n2 == 2020))
    print(pair, pair[0] * pair[1])


def compute2():
    input_nums = puzzle_input(__file__, int)
    triple = next(((n1, n2, n3) for i1, n1 in enumerate(input_nums) for i2, n2 in enumerate(input_nums) for i3, n3 in enumerate(input_nums) if i1 < i2 < i3 and n1 + n2 + n3 == 2020))
    print(triple, triple[0] * triple[1] * triple[2])


if __name__ == '__main__':
    compute1()
    compute2()
