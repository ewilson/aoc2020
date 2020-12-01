from functools import reduce
from operator import mul

from aoc.util import multiline_input, verify


def compute1(nums):
    return next(((n1, n2) for i1, n1 in enumerate(nums) for i2, n2 in enumerate(nums) if i1 < i2 and n1 + n2 == 2020))


def compute2(nums):
    return next(((n1, n2, n3) for i1, n1 in enumerate(nums) for i2, n2 in enumerate(nums) for i3, n3 in enumerate(nums) if i1 < i2 < i3 and n1 + n2 + n3 == 2020))


def compute(nums, f, expected=None):
    value = reduce(mul, f(nums), 1)
    return verify(expected, value)


if __name__ == '__main__':
    data = multiline_input(__file__, tf=int)

    result1 = compute(data, compute1, 138379)
    print(result1)

    result2 = compute(data, compute2, 85491920)
    print(result2)
