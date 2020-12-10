from functools import reduce
from operator import mul

from aoc.util import single_line_records, test_solution


def segment_partition_count(segment):
    """Segment should contain no 'three gaps'"""
    if len(segment) <= 2:
        return 1
    elif len(segment) == 3:
        return 2 if segment[2] - segment[0] <= 3 else 1
    else:
        first, second, third, fourth = segment[0], segment[1], segment[2], segment[3]
        if fourth - first == 3:
            return segment_partition_count(segment[1:]) + segment_partition_count(segment[2:]) + segment_partition_count(segment[3:])
        else:
            return segment_partition_count(segment[1:]) + segment_partition_count(segment[2:])


def find_essential_segments(adapters):
    full = [0] + sorted(adapters)
    essential_points = []
    for idx, val in enumerate(full):
        if idx == 0 or idx == len(full)-1:
            essential_points.append(idx)
        elif val - full[idx-1] == 3 or full[idx+1] - val == 3:
            essential_points.append(idx)
    previous = None
    segments = []
    for idx in essential_points:
        if previous is not None:
            segments.append(full[previous:idx+1])
        previous = idx
    return segments


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
    return ones * threes


def compute2(records):
    essential_segments = find_essential_segments(records)
    return reduce(mul, [segment_partition_count(s) for s in essential_segments], 1)


if __name__ == '__main__':
    test_data = single_line_records(__file__, int, test=True)
    test_data_b = single_line_records(__file__, int, test=True, version='b')
    data = single_line_records(__file__, int)

    test_solution(compute1, test_data, 35)
    test_solution(compute1, test_data_b, 220)
    test_solution(compute1, data, 2244)
    test_solution(compute2, test_data, 8)
    test_solution(compute2, test_data_b, 19208)
    test_solution(compute2, data, 3947645370368)
