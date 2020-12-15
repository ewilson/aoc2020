from aoc.util import regex_parse_input, test_solution


def compute1(records):
    return None


def compute2(records):
    return None


if __name__ == '__main__':
    pattern = r''
    test_data = regex_parse_input(__file__, pattern, test=True)
    data = regex_parse_input(__file__, pattern)

    test_solution(compute1, test_data, 4)
    # test_solution(compute1, data, 326)
    # test_solution(compute2, test_data, 32)
    # test_solution(compute2, data, 5635)
