from aoc.util import single_line_records, test_solution


def parse(lines):
    rules = {}
    messages = []
    for line in lines:
        if ':' in line:
            num, rule = line.split(': ')
            num = int(num)
            if '"' in rule:
                rules[num] = rule[1]
            else:
                stuff = []
                for or_part in rule.split('|'):
                    part = []
                    for rule_num in or_part.split(' '):
                        if rule_num:
                            part.append(int(rule_num))
                    stuff.append(part)
                rules[num] = stuff
        else:
            messages.append(line)
    return rules, messages


def matches_part(message, rules, rule_nums):
    parts = list(rule_nums)
    remainder = message
    while parts:
        partial_match, remainder = matches(remainder, rules, parts.pop(0))
        if not partial_match:
            return False, ''
    return True, remainder


def matches(message, rules, rule):
    if not message:
        return False, ''
    elif isinstance(rule, str):
        if message[0] == rule:
            return True, message[1:]
        else:
            return False, ''
    elif isinstance(rule, int):
        return matches(message, rules, rules[rule])
    elif len(rule) == 1:
        return matches_part(message, rules, rule[0])
    else:
        for option in rule:
            partial_match, remainder = matches_part(message, rules, option)
            if partial_match:
                return True, remainder
        return False, ''


def compute1(raw_data):
    rules, messages = parse(raw_data)
    matching = []
    for message in messages:
        match, remainder = matches(message, rules, rules[0])
        if match and not remainder:
            matching.append(message)
    print(matching)
    return len(matching)


def compute2(records):
    return None


if __name__ == '__main__':
    test_data = single_line_records(__file__, test=True)
    data = single_line_records(__file__)

    test_solution(compute1, test_data, 2)
    test_solution(compute1, data, 178)
    # test_solution(compute2, test_data, 32)
    # test_solution(compute2, data, 5635)
