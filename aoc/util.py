import re
from typing import Callable


def _open_file(filename, test):
    file_prefix = 'test' if test else 'input'
    input_filename = f'data/{file_prefix}{filename[-5:-3]}.txt'
    return open(input_filename)


def _delimited_input(filename, tf=id, delimiter=',', test=False):
    file = _open_file(filename, test)
    return [tf(item) for item in file.read().split(delimiter)]


def single_line_records(filename: str, tf=lambda x: x, test=False):
    return _delimited_input(filename, tf=tf, delimiter='\n', test=test)


def multiple_line_records(filename: str, test=False):
    records = []
    current_record = []
    file = _open_file(filename, test)
    for line in file.readlines():
        if line.strip() == '':
            records.append(' '.join(current_record))
            current_record.clear()
        else:
            current_record.append(line.strip())
    if current_record:
        records.append(' '.join(current_record))
    return records


def regex_parse_input(filename: str, pattern: str, test=False):
    p = re.compile(pattern)
    return single_line_records(filename, tf=lambda line: p.match(line).groups(), test=test)


def test_solution(f: Callable, records: list, expected=None, options=None):
    """
    Applies function to records and tests against expected value.

    Prints result, and throws assertion error if doesn't match expected

    :param f: unary solution function, expects list
    :param records: list, typically parsed into meaningful records
    :param expected: optional expected value, for testing
    :param options: other values needed by the function, if necessary
    :return: None
    """
    result = f(records) if options is None else f(records, options)
    print(result)
    if expected:
        assert result == expected, f'{expected, result}'
