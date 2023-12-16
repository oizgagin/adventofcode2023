def solution(grid):
    UP, DOWN, RIGHT, LEFT = tuple(xrange(0, 4))

    dirs = {UP: (-1, 0), DOWN: (1, 0), RIGHT: (0, 1), LEFT: (0, -1)}
    refs = {
        "/": {UP: RIGHT, DOWN: LEFT, LEFT: DOWN, RIGHT: UP},
        "\\": {UP: LEFT, DOWN: RIGHT, LEFT: UP, RIGHT: DOWN},
    }

    is_valid = lambda p: 0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0])

    get_p = lambda p: grid[p[0]][p[1]]

    move = lambda p, d: (p[0] + d[0], p[1] + d[1])

    q = [((0, -1), RIGHT)]

    seen = set()

    while len(q) > 0:
        q2 = []

        for p, dir_ in q:
            pp = move(p, dirs[dir_])
            if not is_valid(pp):
                continue

            if get_p(pp) == ".":
                q2.append((pp, dir_))
            elif get_p(pp) == "/":
                q2.append((pp, refs["/"][dir_]))
            elif get_p(pp) == "\\":
                q2.append((pp, refs["\\"][dir_]))
            elif get_p(pp) == "|":
                if dir_ in (UP, DOWN):
                    q2.append((pp, dir_))
                else:
                    q2.append((pp, UP))
                    q2.append((pp, DOWN))
            elif get_p(pp) == "-":
                if dir_ in (LEFT, RIGHT):
                    q2.append((pp, dir_))
                else:
                    q2.append((pp, LEFT))
                    q2.append((pp, RIGHT))
            else:
                raise Exception("unreachable")

        q2 = filter(lambda p: p not in seen, q2)
        for v in q2:
            seen.add(v)

        q = q2

    return len(set(map(lambda p: p[0], seen)))


def parse(input):
    return map(list, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
