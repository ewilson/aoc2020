import re

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
            your_ticket.append([int(n) for n in line.split(',')])
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


def compute2(data, prefix):
    restrictions, your_ticket, nearby_tickets = parse(data)
    _, valid_tickets = validate_tickets(nearby_tickets, restrictions)
    return None


if __name__ == '__main__':
    test_data = single_line_records(__file__, test=True)
    test_data_b = single_line_records(__file__, test=True, version='b')
    data = single_line_records(__file__)

    test_solution(compute1, test_data, 71)
    test_solution(compute1, data)
    test_solution(compute2, test_data_b, 11, options='r')
    # test_solution(compute2, data, options='departure')
