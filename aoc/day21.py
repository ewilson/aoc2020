from collections import defaultdict

from aoc.util import regex_parse_input, test_solution


def parse(record):
    return record[0].split(), record[1].split(', ')


def compute1(records):
    lookup = {}
    parsed = [parse(record) for record in records]
    for ingredients, allergens in parsed:
        for a in allergens:
            if a in lookup:
                lookup[a] &= set(ingredients)
            else:
                lookup[a] = set(ingredients)
    possible = set()
    for ingredients in lookup.values():
        possible.update(ingredients)
    count = 0
    for ingredients, _ in parsed:
        for i in ingredients:
            if i not in possible:
                count += 1
    return count


def compute2(records):
    lookup = {}
    parsed = [parse(record) for record in records]
    for ingredients, allergens in parsed:
        for a in allergens:
            if a in lookup:
                lookup[a] &= set(ingredients)
            else:
                lookup[a] = set(ingredients)
    possible = set()
    for ingredients in lookup.values():
        possible.update(ingredients)
    dangerous = set()
    while True:
        allergens = list(lookup.keys())
        for allergen in allergens:
            if len(lookup[allergen]) == 1:
                bad = lookup[allergen].pop()
                dangerous.add((bad, allergen))
                del lookup[allergen]
        for bad, _ in dangerous:
            for allergen in allergens:
                if allergen in lookup and bad in lookup[allergen]:
                    lookup[allergen] -= {bad}
        if len(lookup) == 0:
            break
    return ','.join([ing for ing, allrg in sorted(list(dangerous), key=lambda x: x[1])])


if __name__ == '__main__':
    pattern = r'^([ \w]+) \(contains ([ \w,]+)\)$'
    test_data = regex_parse_input(__file__, pattern, test=True)
    data = regex_parse_input(__file__, pattern)

    test_solution(compute1, test_data, 5)
    test_solution(compute1, data, 2098)
    test_solution(compute2, test_data, 'mxmxvkd,sqjhc,fvjkl')
    test_solution(compute2, data)
