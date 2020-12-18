day = input('Day?\n>>> ')

data_files = [f'input{day}.txt', f'test{day}.txt']

for name in data_files:
    open(f'data/{name}', 'w')

python_file = open(f'day{day}.py', 'w')
python_file.writelines([
    'from aoc.util import regex_parse_input, test_solution\n',
    '\n',
    '\n',
    'def compute1(records):\n',
    '    return None\n',
    '\n',
    '\n',
    'def compute2(records):\n',
    '    return None\n',
    '\n',
    '\n',
    "if __name__ == '__main__':\n",
    "    pattern = r''\n",
    '    test_data = regex_parse_input(__file__, pattern, test=True)\n',
    '    data = regex_parse_input(__file__, pattern)\n\n',
    '    test_solution(compute1, test_data, 4)\n',
    '    # test_solution(compute1, data, 326)\n',
    '    # test_solution(compute2, test_data, 32)\n',
    '    # test_solution(compute2, data, 5635)\n',
])