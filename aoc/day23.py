from aoc.util import regex_parse_input, test_solution


class Node:

    def __init__(self, val, next_val):
        self.val = val
        self.next_val = next_val

    def find_node(self, val):
        if val == self.val:
            return self
        else:
            return self.next_val.find_node(val)

    def order(self, one_found=False, stuff=''):
        if self.val == 1:
            if one_found:
                return stuff
            else:
                return self.next_val.order(one_found=True)
        else:
            if one_found:
                return self.next_val.order(one_found=one_found, stuff=f'{stuff}{self.val}')
            else:
                return self.next_val.order(one_found=one_found)

    def __repr__(self):
        return f'{self.val} -> <{self.next_val.val}>'


def minus_one_circular(num):
    return num - 1 if num > 1 else 9


def turn(current_node):
    next_node = current_node.next_val
    last_removed = current_node.next_val.next_val.next_val
    new_next = current_node.next_val.next_val.next_val.next_val
    current_node.next_val = new_next
    removed_vals = [next_node.val, next_node.next_val.val, next_node.next_val.next_val.val]
    destination = minus_one_circular(current_node.val)
    while destination in removed_vals:
        destination = minus_one_circular(destination)
    destination_node = current_node.find_node(destination)
    old_destination_next = destination_node.next_val
    destination_node.next_val = next_node
    last_removed.next_val = old_destination_next
    return current_node.next_val


def compute1(cups, number_turns):
    nodes = [Node(c, None) for c in cups]
    for i in range(len(nodes)-1):
        nodes[i].next_val = nodes[i+1]
    nodes[len(nodes)-1].next_val = nodes[0]
    current = nodes[0]
    for _ in range(number_turns):
        current = turn(current)
    return current.order()


def compute2(records):
    return None


if __name__ == '__main__':
    test_data = [int(n) for n in '389125467']
    data = [int(n) for n in '198753462']

    test_solution(compute1, test_data, '67384529', options=100)
    test_solution(compute1, data, '62934785', options=100)
    # test_solution(compute1, data, 326)
    # test_solution(compute2, test_data, 32)
    # test_solution(compute2, data, 5635)
