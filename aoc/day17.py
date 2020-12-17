from aoc.util import single_line_records, test_solution


def print_slice(world, xy_dim, z):
    print(f'z = {z}')
    for x in range(xy_dim[0][0], xy_dim[0][1] + 1):
        for y in range(xy_dim[1][0], xy_dim[1][1] + 1):
            print('#' if (x, y, z) in world else '.', end='')
        print()
    print()


def print_slice2(world, xy_dim, z, w):
    print(f'z = {z}, w = {w}')
    for x in range(xy_dim[0][0], xy_dim[0][1] + 1):
        for y in range(xy_dim[1][0], xy_dim[1][1] + 1):
            print('#' if (x, y, z, w) in world else '.', end='')
        print()
    print()


def print_world(world, dimensions):
    z_min, z_max = dimensions[2]
    for z in range(z_max, z_min - 1, -1):
        print_slice(world, dimensions[0:2], z)


def print_world2(world, dimensions):
    z_min, z_max = dimensions[2]
    w_min, w_max = dimensions[3]
    for z in range(z_min, z_max + 1):
        for w in range(w_min, w_max + 1):
            print_slice2(world, dimensions[0:2], z, w)


def build(init_config):
    world = set()
    for i, row in enumerate(init_config):
        for j, cell in enumerate(row):
            if cell == '#':
                world.add((i, j, 0))
    dimensions = ((0, len(init_config[0]) - 1), (0, len(init_config[0]) - 1), (0, 0))
    return world, dimensions


def build2(init_config):
    world = set()
    for i, row in enumerate(init_config):
        for j, cell in enumerate(row):
            if cell == '#':
                world.add((i, j, 0, 0))
    dimensions = ((0, len(init_config[0]) - 1), (0, len(init_config[0]) - 1), (0, 0), (0, 0))
    return world, dimensions


def find_n(coord):
    return [(x, y, z) for x in range(coord[0] - 1, coord[0] + 2) for y in range(coord[1] - 1, coord[1] + 2) for z in
            range(coord[2] - 1, coord[2] + 2) if (x, y, z) != coord]


def find_n2(coord):
    return [(x, y, z, w) for x in range(coord[0] - 1, coord[0] + 2) for y in range(coord[1] - 1, coord[1] + 2) for z in
            range(coord[2] - 1, coord[2] + 2) for w in range(coord[3] - 1, coord[3] + 2) if (x, y, z, w) != coord]


def count_neighbors(world, coord, find_neighbors):
    neighbors = find_neighbors(coord)
    return len([n for n in neighbors if n in world])


def find_dim(world, axis):
    return min(world, key=lambda p: p[axis])[axis], max(world, key=lambda p: p[axis])[axis]


def cycle(world, dimensions):
    to_life = set()
    dying = set()
    for x in range(dimensions[0][0] - 1, dimensions[0][1] + 2):
        for y in range(dimensions[1][0] - 1, dimensions[1][1] + 2):
            for z in range(dimensions[2][0] - 1, dimensions[2][1] + 2):
                n = count_neighbors(world, (x, y, z), find_n)
                if (x, y, z) in world and (n < 2 or n > 3):
                    dying.add((x, y, z))
                elif (x, y, z) not in world and n == 3:
                    to_life.add((x, y, z))
    world.difference_update(dying)
    world.update(to_life)
    return find_dim(world, 0), find_dim(world, 1), find_dim(world, 2)


def cycle2(world, dimensions):
    to_life = set()
    dying = set()
    for x in range(dimensions[0][0] - 1, dimensions[0][1] + 2):
        for y in range(dimensions[1][0] - 1, dimensions[1][1] + 2):
            for z in range(dimensions[2][0] - 1, dimensions[2][1] + 2):
                for w in range(dimensions[3][0] - 1, dimensions[3][1] + 2):
                    n = count_neighbors(world, (x, y, z, w), find_n2)
                    if (x, y, z, w) in world and (n < 2 or n > 3):
                        dying.add((x, y, z, w))
                    elif (x, y, z, w) not in world and n == 3:
                        to_life.add((x, y, z, w))
    world.difference_update(dying)
    world.update(to_life)
    return find_dim(world, 0), find_dim(world, 1), find_dim(world, 2), find_dim(world, 3)


def compute1(init_config):
    world, dimensions = build(init_config)
    for _ in range(6):
        dimensions = cycle(world, dimensions)
    return len(world)


def compute2(init_config):
    world, dimensions = build2(init_config)
    for _ in range(6):
        dimensions = cycle2(world, dimensions)
    return len(world)


if __name__ == '__main__':
    test_data = single_line_records(__file__, list, test=True)
    data = single_line_records(__file__, list)

    test_solution(compute1, test_data, 112)
    test_solution(compute1, data, 384)
    test_solution(compute2, test_data, 848)
    test_solution(compute2, data, 2012)
