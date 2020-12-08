from collections import Counter

from aoc.util import multiple_line_records, verify


def answers(record):
    c = Counter([r for r in record if r != ' '])
    return c.keys()


def answers2(record):
    return set.intersection(*[set(a) for a in record.split()])


def compute1(records, expected=None):
    total = sum([len(answers(r)) for r in records])
    return verify(expected, total)


def compute2(records, expected=None):
    total = sum([len(answers2(r)) for r in records])
    return verify(expected, total)


if __name__ == '__main__':
    test_data = multiple_line_records(__file__, test=True)
    data = multiple_line_records(__file__)
    compute1(test_data, 11)
    compute1(data, 6680)
    compute2(test_data, 6)
    compute2(data, 3117)
