from aoc.util import single_line_records, test_solution


def compute1(lines):
    timestamp = int(lines[0])
    buses = [int(bus_id) for bus_id in lines[1].split(',') if bus_id != 'x']
    wait_times = [(-timestamp % bus_id, bus_id) for bus_id in buses]
    first_time, first_id = min(*wait_times, key=lambda x: x[0])
    return first_time * first_id


def compute2(lines):
    buses = [bus_id for bus_id in lines[1].split(',')]
    remainders = [(int(bus_id), -idx % int(bus_id)) for idx, bus_id in enumerate(buses) if bus_id != 'x']
    divisors, solution = 1, 0
    for bus_id, remainder, in remainders:
        while solution % bus_id != remainder:
            solution += divisors
        divisors *= bus_id
    return solution


if __name__ == '__main__':
    test_data = single_line_records(__file__, test=True)
    data = single_line_records(__file__)

    test_solution(compute1, test_data, 295)
    test_solution(compute1, data, 171)
    test_solution(compute2, test_data, 1068781)
    test_solution(compute2, data, 539746751134958)
