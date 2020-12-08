import re


def open_file(filename, test):
    file_prefix = 'test' if test else 'input'
    input_filename = f'data/{file_prefix}{filename[-5:-3]}.txt'
    return open(input_filename)


def delimited_input(filename, tf=id, delimiter=',', test=False):
    file = open_file(filename, test)
    return [tf(item) for item in file.read().split(delimiter)]


def single_line_records(filename, tf=lambda x: x, test=False):
    return delimited_input(filename, tf=tf, delimiter='\n', test=test)


def multiple_line_records(filename, test=False):
    records = []
    current_record = []
    file = open_file(filename, test)
    for line in file.readlines():
        if line.strip() == '':
            records.append(' '.join(current_record))
            current_record.clear()
        else:
            current_record.append(line.strip())
    if current_record:
        records.append(' '.join(current_record))
    return records


def regex_parse_input(filename, pattern, test=False):
    p = re.compile(pattern)
    return single_line_records(filename, tf=lambda line: p.match(line).groups(), test=test)


def verify(expected, result):
    print(result)
    if expected:
        assert result == expected
    return result
