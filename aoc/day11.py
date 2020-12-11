from aoc.util import single_line_records, test_solution


def find_neighbors(x, y, width, height):
    max_neighbors = [(i, j) for i in range(x-1, x+2) for j in range(y-1, y+2) if (i, j) != (x, y)]
    in_bound_neighbors = [coords for coords in max_neighbors if 0 <= coords[0] < width and 0 <= coords[1] < height]
    return in_bound_neighbors


def next_step(layout):
    new_layout = [list(row) for row in layout]
    for i, row in enumerate(layout):
        for j, spot in enumerate(row):
            if spot != '.':
                neighbors_spots = find_neighbors(j, i, len(row), len(layout))
                num_neighbors = sum([1 for x, y in neighbors_spots if layout[y][x] == '#'])
                if num_neighbors >= 4:
                    new_layout[i][j] = 'L'
                elif num_neighbors == 0:
                    new_layout[i][j] = '#'
    return new_layout


def compute1(layout):
    previous = None
    while layout != previous:
        next_layout = next_step(layout)
        previous = layout
        layout = next_layout
    return sum([1 for r in layout for s in r if s == '#'])


def compute2(records):
    return None


if __name__ == '__main__':
    test_data = single_line_records(__file__, list, test=True)
    data = single_line_records(__file__, list)

    test_solution(compute1, test_data, 37)
    test_solution(compute1, data)
    # test_solution(compute2, test_data, 26)
    # test_solution(compute2, data)
