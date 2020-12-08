from sys import argv

day = argv[1]

data_files = [f'day{day}.py', f'input{day}.txt', f'test{day}.txt']

for name in data_files:
    open(name, 'w')

python_file = open(f'day{day}.py', 'w')
python_file.writelines([
    'from aoc.util import regex_parse_input, verify\n',
    '\n',
    '\n',
    'def compute1(records, expected=None):\n',
    '    return verify(expected, None)\n',
    '\n',
    '\n',
    'def compute2(records, expected=None):\n',
    '    return verify(expected, None)\n',
    '\n',
    '\n',
    "if __name__ == '__main__':\n",
    "    pattern = r''\n",
    '    test_data = regex_parse_input(__file__, pattern, test=True)\n',
    '    data = regex_parse_input(__file__, pattern)\n',
    '    compute1(test_data, 4)\n',
    '    # result1 = compute1(data, 326)\n',
    '    # print(result1)\n',
    '    # compute2(test_data, 32)\n',
    '    # result2 = compute2(data, 5635)\n',
    '    # print(result2)\n'
])