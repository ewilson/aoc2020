from operator import add, mul

from aoc.util import single_line_records, test_solution


def build_pf(expression):
    symbols = [c for c in expression if c != ' ']
    output = []
    operators = []
    for s in symbols:
        if s.isdigit():
            output.append(s)
        if s in '+*':
            if operators and operators[-1] in '+*':
                output.append(operators.pop())
            operators.append(s)
        if s == '(':
            operators.append(s)
        if s == ')':
            while operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()

    while operators:
        output.append(operators.pop())
    postfix = []
    for s in output:
        if s.isdigit():
            postfix.append(int(s))
        if s == '+':
            postfix.append(add)
        if s == '*':
            postfix.append(mul)

    return postfix


def build_pf2(expression):
    symbols = [c for c in expression if c != ' ']
    output = []
    operators = []
    for s in symbols:
        if s.isdigit():
            output.append(s)
        if s in '+*':
            while operators and operators[-1] == '+':
                output.append(operators.pop())
            operators.append(s)
        if s == '(':
            operators.append(s)
        if s == ')':
            while operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()

    while operators:
        output.append(operators.pop())
    postfix = []
    for s in output:
        if s.isdigit():
            postfix.append(int(s))
        if s == '+':
            postfix.append(add)
        if s == '*':
            postfix.append(mul)

    return postfix


def evaluate(postfix):
    stack = []
    for item in postfix:
        if isinstance(item, int):
            stack.append(item)
        else:
            stack.append(item(stack.pop(), stack.pop()))
    return stack[0]


def compute1(lines):
    postfix = [build_pf(line) for line in lines]
    results = [evaluate(p) for p in postfix]
    return sum(results)


def compute2(lines):
    postfix = [build_pf2(line) for line in lines]
    results = [evaluate(p) for p in postfix]
    return sum(results)


if __name__ == '__main__':
    test_data = single_line_records(__file__, test=True)
    data = single_line_records(__file__)

    test_solution(compute1, test_data, 26457)
    test_solution(compute1, data, 23507031841020)
    test_solution(compute2, test_data, 694173)
    test_solution(compute2, data, 218621700997826)
