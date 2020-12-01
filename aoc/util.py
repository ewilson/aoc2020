def puzzle_input(filename, tf=id):
    input_filename = f'input{filename[-5:-3]}.txt'
    lines = open(input_filename)
    return [tf(line) for line in lines.readlines()]
