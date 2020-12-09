from aoc.util import single_line_records, test_solution


def valid(num, nums):
    for a in nums:
        for b in nums:
            if a+b == num and a!=b:
                return True
    return False


def find_invalid(records, preamble_length):
    return next((n for idx, n in enumerate(records) if idx >= preamble_length and not valid(n, records[idx-preamble_length:idx])))


def find_contiguous(records, invalid):
    start, end = 0, 1
    total = records[start]
    while total != invalid:
        total += records[end]
        if total < invalid:
            end += 1
        elif total > invalid:
            start += 1
            end = start + 1
            total = records[start]
    return records[start:end+1]


def compute1(records, preamble_length):
    return find_invalid(records, preamble_length)


def compute2(records, preamble_length):
    invalid = find_invalid(records, preamble_length)
    contiguous = find_contiguous(records, invalid)
    return min(contiguous) + max(contiguous)


if __name__ == '__main__':
    pattern = r''
    test_data = single_line_records(__file__, int, test=True)
    data = single_line_records(__file__, int)

    test_solution(compute1, test_data, 127, options=5)
    test_solution(compute1, data, 1038347917, options=25)
    test_solution(compute2, test_data, 62, options=5)
    test_solution(compute2, data, 137394018, options=25)
