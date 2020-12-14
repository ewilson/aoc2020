from aoc.util import regex_parse_input, test_solution


def compute1(instructions):
    mask = ''
    mem = {}
    for inst, val in instructions:
        if inst == 'mask':
            mask = val
        else:
            location = inst[4:-1]
            binary = f'{int(val):036b}'
            masked_val = ''.join([mask[i] if mask[i] != 'X' else binary[i] for i in range(36)])
            mem[location] = int(masked_val, 2)
    return sum([mem[k] for k in mem])


def combinations(n):
    if n == 1:
        return ['0', '1']
    else:
        previous = combinations(n-1)
        return ['0' + n for n in previous] + ['1' + n for n in previous]


def build_masked_loc(location, mask):
    binary_loc = f'{int(location):036b}'
    return ''.join([binary_loc[i] if mask[i] == '0' else mask[i] for i in range(36)])


def compute2(instructions):
    mask = ''
    mem = {}
    for inst, val in instructions:
        if inst == 'mask':
            mask = val
        else:
            masked_loc = build_masked_loc(inst[4:-1], mask)
            possibilities = combinations(masked_loc.count('X'))
            locations = []
            for p in possibilities:
                mask_values = list(p)
                locations.append(''.join([c if c != 'X' else mask_values.pop() for c in masked_loc]))
            for loc in locations:
                mem[int(loc, 2)] = int(val)
    return sum([mem[k] for k in mem])


if __name__ == '__main__':
    pattern = r'(.+) = ([X0-9]+)'
    test_data = regex_parse_input(__file__, pattern, test=True)
    test_data_b = regex_parse_input(__file__, pattern, test=True, version='b')
    data = regex_parse_input(__file__, pattern)

    test_solution(compute1, test_data, 165)
    test_solution(compute1, data, 6386593869035)
    test_solution(compute2, test_data_b, 208)
    test_solution(compute2, data, 4288986482164)
