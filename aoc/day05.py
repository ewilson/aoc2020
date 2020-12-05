from aoc.util import multiline_input, verify


def from_binary(s, one):
    return int(''.join(['1' if c == one else '0' for c in s]), 2)


def locate(line):
    row_info, col_info = line[:7], line[-3:]
    return from_binary(row_info, 'B'), from_binary(col_info, 'R')


def seat_id(row, col):
    return 8*row + col


def all_ids(lines):
    return [seat_id(*locate(line)) for line in lines]


def compute1(stuff, expected=None):
    largest_id = max(all_ids(stuff))
    return verify(expected, largest_id)


def compute2(stuff, expected=None):
    seats = sorted(all_ids(stuff))
    previous, your_seat = 0, None
    for s in seats:
        if s - previous == 2:
            your_seat = s-1
        previous = s
    return verify(expected, your_seat)


if __name__ == '__main__':
    test_data = multiline_input(__file__, test=True)
    data = multiline_input(__file__)
    compute1(test_data, 820)
    result1 = compute1(data, 998)
    print(result1)
    result2 = compute2(data, 676)
    print(result2)
