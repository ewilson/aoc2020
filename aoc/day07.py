from aoc.util import regex_parse_input, verify


def bag_tuple(bi):
    parts = bi.split()
    return int(parts[0]), f'{parts[1]} {parts[2]}'


def parse_rules(records):
    def bags(bag_info):
        if bag_info == 'no other bags':
            return []
        else:
            return [bag_tuple(bi) for bi in bag_info.split(',')]
    return {r[0]: bags(r[1]) for r in records}


def build_graph(rules):
    graph = {}
    for rule in rules:
        for num, bag in rules[rule]:
            graph[(rule, bag)] = num
    return graph


def find_parents(bag, graph):
    parents = set()
    for parent, child in graph:
        if child == bag:
            parents.add(parent)
    return parents


def find_ancestors(bag, graph):
    ancestors = set([bag])
    checked = set()
    while ancestors - checked:
        current = next(iter(ancestors - checked))
        ancestors.update(find_parents(current, graph))
        checked.add(current)
    return ancestors - {bag}


def count_descendants(bag, graph):
    descendants = 0
    for parent, child in graph:
        if parent == bag:
            val = graph[(parent, child)]
            descendants += val
            descendants += val*count_descendants(child, graph)
    return descendants


def compute1(records, expected=None):
    rule_dict = parse_rules(records)
    graph = build_graph(rule_dict)
    my_bag = 'shiny gold'
    containing = find_ancestors(my_bag, graph)
    return verify(expected, len(containing))


def compute2(records, expected=None):
    rule_dict = parse_rules(records)
    graph = build_graph(rule_dict)
    my_bag = 'shiny gold'
    contains = count_descendants(my_bag, graph)
    return verify(expected, contains)


if __name__ == '__main__':
    pattern = r'^(.+) bags contain (.+)\.$'
    test_data = regex_parse_input(__file__, pattern, test=True)
    data = regex_parse_input(__file__, pattern)
    compute1(test_data, 4)
    result1 = compute1(data, 326)
    print(result1)
    compute2(test_data, 32)
    result2 = compute2(data)
    print(result2)
