from aoc.util import puzzle_input


def compute1():
    input_nums = puzzle_input(__file__, int)
    for n1 in range(len(input_nums)):
        for n2 in range(n1, len(input_nums)):
            if input_nums[n1] + input_nums[n2] == 2020:
                print(input_nums[n1], input_nums[n2])
                print(input_nums[n1] * input_nums[n2])


def compute2():
    input_nums = puzzle_input(__file__, int)
    for n1 in range(len(input_nums)):
        for n2 in range(n1, len(input_nums)):
            for n3 in range(n2, len(input_nums)):
                if input_nums[n1] + input_nums[n2] + input_nums[n3] == 2020:
                    print(input_nums[n1], input_nums[n2], input_nums[n3])
                    print(input_nums[n1] * input_nums[n2] * input_nums[n3])


if __name__ == '__main__':
    compute1()
    compute2()
