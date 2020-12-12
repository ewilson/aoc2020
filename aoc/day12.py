from aoc.util import regex_parse_input, test_solution


def navigate(ship, instructions):
    for inst in instructions:
        ship.navigate(*inst)
    return ship.manhattan()


def compute1(instructions):
    s = Ship()
    return navigate(s, instructions)


def compute2(instructions):
    s = Ship2()
    return navigate(s, instructions)


class Ship:

    def __init__(self):
        self.ship_direction = 0
        self.position_x = 0
        self.position_y = 0

    def navigate(self, first, second):
        if first in 'NEWS':
            self._compass_move(first, int(second))
        elif first in 'LR':
            self._turn(first, int(second))
        elif first == 'F':
            self._forward_move(int(second))

    def manhattan(self):
        return abs(self.position_x) + abs(self.position_y)

    def _compass_move(self, move_direction, distance):
        if move_direction == 'E':
            self.position_x += distance
        elif move_direction == 'N':
            self.position_y += distance
        elif move_direction == 'W':
            self.position_x -= distance
        elif move_direction == 'S':
            self.position_y -= distance

    def _forward_move(self, distance):
        if self.ship_direction == 0:
            self.position_x += distance
        elif self.ship_direction == 90:
            self.position_y += distance
        elif self.ship_direction == 180:
            self.position_x -= distance
        elif self.ship_direction == 270:
            self.position_y -= distance

    def _turn(self, direction, degrees):
        angle = (1 if direction == 'L' else -1) * degrees
        self.ship_direction += angle
        self.ship_direction %= 360


class Ship2:

    def __init__(self):
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.position_x = 0
        self.position_y = 0

    def navigate(self, first, second):
        if first in 'NEWS':
            self._move_waypoint(first, int(second))
        elif first in 'LR':
            self._rotate_waypoint(first, int(second))
        elif first == 'F':
            self._to_waypoint(int(second))

    def manhattan(self):
        return abs(self.position_x) + abs(self.position_y)

    def _move_waypoint(self, move_direction, distance):
        if move_direction == 'E':
            self.waypoint_x += distance
        elif move_direction == 'N':
            self.waypoint_y += distance
        elif move_direction == 'W':
            self.waypoint_x -= distance
        elif move_direction == 'S':
            self.waypoint_y -= distance

    def _to_waypoint(self, times):
        self.position_x += times * self.waypoint_x
        self.position_y += times * self.waypoint_y

    def _rotate_waypoint(self, direction, degrees):
        left_quarter_turns = (degrees//90 if direction == 'L' else -degrees//90) % 4
        if left_quarter_turns == 1:
            self.waypoint_x, self.waypoint_y = -self.waypoint_y, self.waypoint_x
        elif left_quarter_turns == 2:
            self.waypoint_x, self.waypoint_y = -self.waypoint_x, -self.waypoint_y
        elif left_quarter_turns == 3:
            self.waypoint_x, self.waypoint_y = self.waypoint_y, -self.waypoint_x


if __name__ == '__main__':
    pattern = r'^(\w)(\d+)$'
    test_data = regex_parse_input(__file__, pattern, test=True)
    data = regex_parse_input(__file__, pattern)

    test_solution(compute1, test_data, 25)
    test_solution(compute1, data)
    test_solution(compute2, test_data, 286)
    test_solution(compute2, data)
