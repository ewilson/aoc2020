from collections import Counter

from aoc.util import multiline_input


def compute1(data):
    return len([d for d in data if validate(d[0], d[1])])


def validate(policy, password):
    minmax, char = policy.split(' ')
    minmaxl = minmax.split('-')
    minc = int(minmaxl[0])
    maxc = int(minmaxl[1])
    pwc = Counter(password)
    return minc <= pwc[char] <= maxc


def validate2(policy, password):
    onetwo, char = policy.split(' ')
    onetwol = onetwo.split('-')
    one = int(onetwol[0])
    two = int(onetwol[1])
    print(policy, password, password[one-1] == char and password[two-1] != char)
    print(f'character {one} is {char} ({password[one-1]}), character {two} ({password[two-1]}) is twot')
    return (password[one-1] == char and password[two-1] != char) or (password[one-1] != char and password[two-1] == char)


def compute2(nums):
    return len([d for d in data if validate2(d[0], d[1])])


# 3-8 v: knvrrqvtv
if __name__ == '__main__':
    data = multiline_input(__file__, lambda line: line.split(': '))
    result1 = compute1(data)
    print(result1)
    result2 = compute2(data)
    print(result2)
