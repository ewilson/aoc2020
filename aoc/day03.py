from aoc.util import single_line_records, test_solution


def compute1(forest):
    x, y = 0, 0
    hits = 0
    width = len(forest[0])
    for row in forest:
        if row[x % width] == '#':
            hits += 1
        x += 3
    return hits


def compute2(forest):
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
    return hit_prod


if __name__ == '__main__':
    test_data = single_line_records(__file__, test=True)
    data = single_line_records(__file__)

    test_solution(compute1, test_data, 7)
    test_solution(compute1, data, 151)
    test_solution(compute2, test_data, 336)
    test_solution(compute2, data, 7540141059)
