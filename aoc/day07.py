from aoc.util import regex_parse_input, test_solution


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


def find_ancestors(bag, graph):
    ancestors = set()
    for parent, child in graph:
        if child == bag:
            ancestors.add(parent)
            ancestors.update(find_ancestors(parent, graph))
    return ancestors


def count_descendants(bag, graph):
    descendants = 0
    for parent, child in graph:
        if parent == bag:
            val = graph[(parent, child)]
            descendants += val
            descendants += val*count_descendants(child, graph)
    return descendants


def compute1(records):
    rule_dict = parse_rules(records)
    graph = build_graph(rule_dict)
    my_bag = 'shiny gold'
    return len(find_ancestors(my_bag, graph))


def compute2(records):
    rule_dict = parse_rules(records)
    graph = build_graph(rule_dict)
    my_bag = 'shiny gold'
    return count_descendants(my_bag, graph)


if __name__ == '__main__':
    pattern = r'^(.+) bags contain (.+)\.$'
    test_data = regex_parse_input(__file__, pattern, test=True)
    data = regex_parse_input(__file__, pattern)

    test_solution(compute1, test_data, 4)
    test_solution(compute1, data, 326)
    test_solution(compute2, test_data, 32)
    test_solution(compute2, data, 5635)
