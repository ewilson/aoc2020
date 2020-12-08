from collections import Counter

from aoc.util import regex_parse_input, verify


def compute1(data, expected=None):
    return verify(expected, len([d for d in data if validate(*d)]))


def compute2(data, expected=None):
    return verify(expected, len([d for d in data if validate2(*d)]))


def validate(first, second, char, pw):
    minc = int(first)
    maxc = int(second)
    pwc = Counter(pw)
    return minc <= pwc[char] <= maxc


def validate2(first, second, char, pw):
    one = int(first)
    two = int(second)
    return (pw[one-1] == char and pw[two-1] != char) or (pw[one-1] != char and pw[two-1] == char)


if __name__ == '__main__':
    pattern = r'(\d+)-(\d+) (\w): (\w+)'  
    test_data = regex_parse_input(__file__, pattern, test=True)
    data = regex_parse_input(__file__, pattern)
    compute1(test_data, 2)
    compute1(data, 636)
    compute2(test_data, 1)
    compute2(data, 588)
