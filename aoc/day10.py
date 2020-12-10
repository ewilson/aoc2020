from aoc.util import single_line_records, test_solution


def compute1(records):
    sorted_adapters = sorted(records)
    previous = 0
    ones = 0
    threes = 1
    for adapter in sorted_adapters:
        if adapter - previous == 1:
            ones += 1
        elif adapter - previous == 3:
            threes += 1
        previous = adapter
    print(f'threes: {threes}, size: {len(records)}')
    return ones * threes


def compute2(records):
    return None


if __name__ == '__main__':
    test_data = single_line_records(__file__, int, test=True)
    test_data_b = single_line_records(__file__, int, test=True, version='b')
    data = single_line_records(__file__, int)

    test_solution(compute1, test_data, 35)
    test_solution(compute1, test_data_b, 220)
    test_solution(compute1, data, 2244)
    # test_solution(compute2, test_data, 8)
    # test_solution(compute2, test_data_b, 19208)
    # test_solution(compute2, data)
