def delimited_input(filename, tf=id, delimiter=','):
    input_filename = f'input{filename[-5:-3]}.txt'
    file = open(input_filename)
    return [tf(item) for item in file.read().split(delimiter)]


def multiline_input(filename, tf=id):
    return delimited_input(filename, tf=tf, delimiter='\n')


def verify(expected, result):
    if expected:
        assert result == expected
    return result
