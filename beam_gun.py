from fractions import Fraction as fr


def solution(dimensions, your_position, guard_position, distance):
    l, w = dimensions
    a, b = your_position
    u, v = guard_position
    n_max, m_max = distance // (2 * l) + 1, distance // (2 * w) + 1

    class point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

            self.dist = (x - a) ** 2 + (y - b) ** 2
            if y == b:
                self.slope = "Horizontal"
            else:
                self.slope = fr(x - a, y - b)

            self.right = x > a or (x == a and y > b)

        def way(self):
            return (self.slope, self.right)

    guard = [point(2 * l * n + x, 2 * w * m + y) for n in range(-n_max, n_max + 1) for m in range(-m_max, m_max + 1) for
             x in (-u, u) for y in (-v, v)]
    me = [point(2 * l * n + x, 2 * w * m + y) for n in range(-n_max, n_max + 1) for m in range(-m_max, m_max + 1) for x
          in (-a, a) for y in (-b, b) if (2 * l * n + x, 2 * w * m + y) != your_position]
    directions = {}
    for point in guard:
        if point.dist <= distance ** 2:
            if point.way() in directions:
                directions[point.way()] = min(directions[point.way()], point.dist)
            else:
                directions[point.way()] = point.dist

    for point in me:
        if point.way() in directions:
            if point.dist < directions[point.way()]:
                directions.pop(point.way())

    return len(directions)


if __name__ == "__main__":
    assert solution([3, 2], [1, 1], [2, 1], 4) == 7
