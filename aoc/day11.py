from aoc.util import single_line_records, test_solution


def in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def find_neighbors(x, y, width, height):
    max_neighbors = [(i, j) for i in range(x-1, x+2) for j in range(y-1, y+2) if (i, j) != (x, y)]
    return [coords for coords in max_neighbors if in_bounds(coords[0], coords[1], width, height)]


def find_directions():
    return [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]


def in_direction(x, y, layout, direction):
    current = (x, y)
    while in_bounds(current[0] + direction[0], current[1] + direction[1], len(layout[0]), len(layout)):
        new_location = (current[0] + direction[0], current[1] + direction[1])
        if layout[new_location[1]][new_location[0]] != '.':
            return layout[new_location[1]][new_location[0]]
        current = new_location
    return None


def find_visible(x, y, layout):
    directions = find_directions()
    return [in_direction(x, y, layout, direction) for direction in directions]


def determine_new_status(j, i, layout):
    neighbors_spots = find_neighbors(j, i, len(layout[0]), len(layout))
    num_neighbors = sum([1 for x, y in neighbors_spots if layout[y][x] == '#'])
    if num_neighbors >= 4:
        return 'L'
    elif num_neighbors == 0:
        return '#'
    else:
        return None


def determine_new_status2(j, i, layout):
    visible_seats = find_visible(j, i, layout)
    num_visible = sum([1 for seat in visible_seats if '#' == seat])
    if num_visible >= 5:
        return 'L'
    elif num_visible == 0:
        return '#'
    else:
        return None


def next_step(layout, status):
    new_layout = [list(row) for row in layout]
    for i, row in enumerate(layout):
        for j, spot in enumerate(row):
            if spot != '.':
                new_status = status(j, i, layout)
                if new_status:
                    new_layout[i][j] = new_status
    return new_layout


def determine_final_state(layout, status):
    previous = None
    count = 0
    while layout != previous:
        next_layout = next_step(layout, status)
        previous = layout
        layout = next_layout
        count += 1
    return sum([1 for r in layout for s in r if s == '#'])


def compute1(layout):
    return determine_final_state(layout, determine_new_status)


def compute2(layout):
    return determine_final_state(layout, determine_new_status2)


if __name__ == '__main__':
    test_data = single_line_records(__file__, list, test=True)
    data = single_line_records(__file__, list)

    test_solution(compute1, test_data, 37)
    test_solution(compute1, data, 2254)
    test_solution(compute2, test_data, 26)
    test_solution(compute2, data, 2004)
