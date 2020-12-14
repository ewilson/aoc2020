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


def compute2(records):
    return None


if __name__ == '__main__':
    pattern = r'(.+) = ([X0-9]+)'
    test_data = regex_parse_input(__file__, pattern, test=True)
    data = regex_parse_input(__file__, pattern)

    test_solution(compute1, test_data, 165)
    test_solution(compute1, data, 6386593869035)
    # test_solution(compute2, test_data, 32)
    # test_solution(compute2, data, 5635)
