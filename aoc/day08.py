from aoc.util import single_line_records, verify


def execute(op, val):
    return val if op == 'jmp' else 1, val if op == 'acc' else 0


def run_program(ops):
    accumulator, pointer, executed = 0, 0, set()
    while pointer not in executed and pointer < len(ops):
        executed.add(pointer)
        change_pointer, add = execute(*ops[pointer])
        accumulator += add
        pointer += change_pointer
    return accumulator, pointer == len(ops)


def compute1(ops, expected=None):
    accumulator, terminate = run_program(ops)
    assert not terminate
    return verify(expected, accumulator)


def swap_op(op, val):
    return ('nop', val) if op == 'jmp' else ('jmp', val)


def compute2(ops, expected=None):
    for idx, (op, val) in enumerate(ops):
        if op != 'acc':
            new_ops = list(ops)
            new_ops[idx] = swap_op(op, val)
            accumulator, terminate = run_program(new_ops)
            if terminate:
                return verify(expected, accumulator)
    assert False


if __name__ == '__main__':
    def transform(line):
        first, second = line.split()
        return first, int(second)
    test_data = single_line_records(__file__, tf=transform, test=True)
    data = single_line_records(__file__, tf=transform)
    compute1(test_data, 5)
    result1 = compute1(data, 1394)
    print(result1)
    compute2(test_data, 8)
    result2 = compute2(data, 1626)
    print(result2)
