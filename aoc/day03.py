from aoc.util import single_line_records, verify


def compute1(forest, expected=None):
    x, y = 0, 0
    hits = 0
    width = len(forest[0])
    for row in forest:
        if row[x % width] == '#':
            hits += 1
        x += 3
    return verify(expected, hits)


def compute2(forest, expected=None):
    hit_prod = 1
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        across, down = slope
        x, y = 0, 0
        hits = 0
        width = len(forest[0])
        for idx, row in enumerate(forest):
            if idx % down != 0:
                continue
            if row[x % width] == '#':
                hits += 1
            x += across
        hit_prod *= hits
    return verify(expected, hit_prod)


if __name__ == '__main__':
    test_data = single_line_records(__file__, test=True)
    data = single_line_records(__file__)
    compute1(test_data, 7)
    result1 = compute1(data, 151)
    print(result1)
    compute2(test_data, 336)
    result2 = compute2(data, 7540141059)
    print(result2)
