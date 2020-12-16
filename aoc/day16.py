import re
from functools import reduce
from operator import mul

import numpy as np

from aoc.util import single_line_records, test_solution


def parse_restriction(line):
    pattern = r'(.+): (\d+)-(\d+) or (\d+)-(\d+)'
    p = re.compile(pattern)
    stuff = p.match(line).groups()
    range1 = [n for n in range(int(stuff[1]), int(stuff[2])+1)]
    range2 = [n for n in range(int(stuff[3]), int(stuff[4])+1)]
    return stuff[0], range1+range2


def parse(data_lines):
    restrictions, your_ticket, nearby_tickets = {}, [], []
    section = 0
    for line in data_lines:
        if line == 'your ticket:':
            section = 1
            continue
        elif line == 'nearby tickets:':
            section = 2
            continue
        if section == 0:
            key, val = parse_restriction(line)
            restrictions[key] = val
        if section == 1:
            your_ticket = [int(n) for n in line.split(',')]
        elif section == 2:
            nearby_tickets.append([int(n) for n in line.split(',')])
    return restrictions, your_ticket, nearby_tickets


def validate_tickets(nearby_tickets, restrictions):
    total_invalid = 0
    valid_tickets = []
    for ticket in nearby_tickets:
        valid_ticket = True
        for num in ticket:
            valid_num = False
            for r in restrictions:
                if num in restrictions[r]:
                    valid_num = True
            if not valid_num:
                total_invalid += num
                valid_ticket = False
        if valid_ticket:
            valid_tickets.append(ticket)
    return total_invalid, valid_tickets


def compute1(data):
    restrictions, your_ticket, nearby_tickets = parse(data)
    invalid, _ = validate_tickets(nearby_tickets, restrictions)
    return invalid


def build_sudoku(restrictions, valid_tickets):
    size = len(restrictions)
    grid = np.full((size, size), None)
    for ticket in valid_tickets:
        for i, key in enumerate(restrictions):
            for j, value in enumerate(ticket):
                if value not in restrictions[key]:
                    grid[i][j] = 0
    return grid


def solve_sudoku(grid):
    height, width = grid.shape
    for i in range(height):
        empty_spots = np.where(grid[i] == None)[0]
        one_spot = np.where(grid[i] == 1)[0]
        if len(empty_spots) == 1 and len(one_spot) == 0:
            grid[i][empty_spots[0]] = 1
    for j in range(width):
        empty_spots = np.where(grid[:, j] == None)[0]
        one_spot = np.where(grid[:, j] == 1)[0]
        if len(empty_spots) == 1 and len(one_spot) == 0:
            grid[empty_spots[0]][j] = 1

    for i in range(height):
        one_spot = np.where(grid[i] == 1)[0]
        if len(one_spot) == 1:
            for j in range(width):
                if j != one_spot[0]:
                    grid[i][j] = 0
    for j in range(width):
        one_spot = np.where(grid[:, j] == 1)[0]
        if len(one_spot) == 1:
            for i in range(width):
                if i != one_spot[0]:
                    grid[i][j] = 0
    if np.count_nonzero(grid == None):
        return solve_sudoku(grid)
    else:
        return grid


def find_prefix_fields(grid, prefix, restrictions, your_ticket):
    prefix_fields = []
    for i, key in enumerate(restrictions):
        if key.startswith(prefix):
            field_idx = np.where(grid[i] == 1)[0][0]
            prefix_fields.append(your_ticket[field_idx])
    return prefix_fields


def compute2(data, prefix):
    restrictions, your_ticket, nearby_tickets = parse(data)
    _, valid_tickets = validate_tickets(nearby_tickets, restrictions)
    grid = build_sudoku(restrictions, valid_tickets)
    grid = solve_sudoku(grid)
    prefix_fields = find_prefix_fields(grid, prefix, restrictions, your_ticket)
    return reduce(mul, prefix_fields, 1)


if __name__ == '__main__':
    test_data = single_line_records(__file__, test=True)
    test_data_b = single_line_records(__file__, test=True, version='b')
    data = single_line_records(__file__)

    test_solution(compute1, test_data, 71)
    test_solution(compute1, data, 24110)
    test_solution(compute2, test_data_b, 11, options='r')
    test_solution(compute2, data, 6766503490793, options='departure')
