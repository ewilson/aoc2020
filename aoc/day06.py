from collections import Counter

from aoc.util import multiple_line_records, test_solution


def answers(record):
    c = Counter([r for r in record if r != ' '])
    return c.keys()


def answers2(record):
    return set.intersection(*[set(a) for a in record.split()])


def compute1(records):
    return sum([len(answers(r)) for r in records])


def compute2(records):
    return sum([len(answers2(r)) for r in records])


if __name__ == '__main__':
    test_data = multiple_line_records(__file__, test=True)
    data = multiple_line_records(__file__)

    test_solution(compute1, test_data, 11)
    test_solution(compute1, data, 6680)
    test_solution(compute2, test_data, 6)
    test_solution(compute2, data, 3117)
