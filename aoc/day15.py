from aoc.util import test_solution


def compute1(numbers, end_num):
    last_time = {n: [idx+1] for idx, n in enumerate(numbers)}
    start_turn = len(numbers) + 1
    previous_number = numbers[-1]
    for turn in range(start_turn, end_num + 1):
        previous_number_record = last_time[previous_number]
        if len(previous_number_record) == 1:
            new_number = 0
        else:
            new_number = previous_number_record[-1] - previous_number_record[-2]
        if new_number in last_time:
            last_time[new_number].append(turn)
        else:
            last_time[new_number] = [turn]
        previous_number = new_number
    return new_number


def compute2(numbers, end_num):
    last_time = {n: idx+1 for idx, n in enumerate(numbers)}
    start_turn = len(numbers) + 1
    next_number = 0
    for turn in range(start_turn, end_num):
        if next_number in last_time:
            diff = turn - last_time[next_number]
            last_time[next_number] = turn
            next_number = diff
        else:
            last_time[next_number] = turn
            next_number = 0
    return next_number


if __name__ == '__main__':
    test_data = [0, 3, 6]
    test_data1 = [1, 3, 2]
    test_data2 = [2, 1, 3]
    test_data3 = [1, 2, 3]
    test_data4 = [2, 3, 1]
    test_data5 = [3, 2, 1]
    test_data6 = [3, 1, 2]
    data = [2, 0, 6, 12, 1, 3]

    test_solution(compute2, test_data, 436, options=2020)
    test_solution(compute2, test_data2, 10, options=2020)
    test_solution(compute2, test_data3, 27, options=2020)
    test_solution(compute2, test_data4, 78, options=2020)
    test_solution(compute2, test_data5, 438, options=2020)
    test_solution(compute2, test_data6, 1836, options=2020)

    test_solution(compute2, data, 1428, options=2020)
    test_solution(compute2, data, 3718541, options=30000000)
