from functools import reduce
from operator import mul

from aoc.util import single_line_records, test_solution


def compute1(nums):
    return next(((n1, n2) for i1, n1 in enumerate(nums) for i2, n2 in enumerate(nums) if i1 < i2 and n1 + n2 == 2020))


def compute2(nums):
    return next(((n1, n2, n3) for i1, n1 in enumerate(nums) for i2, n2 in enumerate(nums) for i3, n3 in enumerate(nums) if i1 < i2 < i3 and n1 + n2 + n3 == 2020))


def compute(nums, f):
    return reduce(mul, f(nums), 1)


if __name__ == '__main__':
    test_data = single_line_records(__file__, tf=int, test=True)
    data = single_line_records(__file__, tf=int)

    test_solution(lambda records: compute(data, compute1), test_data, 514579)
    test_solution(lambda records: compute(data, compute1), data, 138379)
    test_solution(lambda records: compute(data, compute2), test_data, 241861950)
    test_solution(lambda records: compute(data, compute2), data, 85491920)
