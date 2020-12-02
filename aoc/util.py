import re


def delimited_input(filename, tf=id, delimiter=',', test=False):
    input_filename = f'test{filename[-5:-3]}.txt' if test else f'input{filename[-5:-3]}.txt'
    file = open(input_filename)
    return [tf(item) for item in file.read().split(delimiter)]


def multiline_input(filename, tf=id, test=False):
    return delimited_input(filename, tf=tf, delimiter='\n', test=test)


def regex_parse_input(filename, pattern, test=False):
    p = re.compile(pattern)
    return multiline_input(filename, lambda line: p.match(line).groups(), test)


def verify(expected, result):
    if expected:
        assert result == expected
    return result
