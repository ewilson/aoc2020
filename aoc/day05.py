from aoc.util import multiline_input, verify


def locate(line):
    row_info = line[:7]
    row_b = ''.join(['1' if r == 'B' else '0' for r in row_info])
    col_info = line[-3:]
    col_b = ''.join(['1' if c == 'R' else '0' for c in col_info])
    col = int(col_b, 2)
    row = int(row_b, 2)
    return row, col


def seat_id(row, col):
    return 8*row + col


def compute1(stuff, expected=None):
    largest_id = max([seat_id(*locate(line)) for line in stuff])
    return verify(expected, largest_id)


def compute2(stuff, expected=None):
    seats = sorted([seat_id(*locate(line)) for line in stuff])
    previous = 0
    for s in seats:
        if s - previous == 2:
            print(previous, s)
        previous = s


if __name__ == '__main__':
    test_data = multiline_input(__file__, test=True)
    data = multiline_input(__file__)
    compute1(test_data, 820)
    result1 = compute1(data)
    print(result1)
    compute2(data)
