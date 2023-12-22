from collections import defaultdict


def solution(bricks):

    def cubes(b):
        sx, sy, sz = b[0]
        ex, ey, ez = b[1]

        for x in xrange(sx, ex+1):
            for y in xrange(sy, ey+1):
                for z in xrange(sz, ez+1):
                    yield (x, y, z)

    def coords_down(b):
        sx, sy, sz = b[0]
        ex, ey, ez = b[1]
        return ((sx, sy, sz-1), (ex, ey, ez-1))

    grid = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: -1)))

    def can_place(b, id_):
        return b[0][2] > 0 and b[1][2] > 0 and all(grid[x][y][z] in (-1, id_) for x, y, z in cubes(b))

    def clear(b, id_):
        for x, y, z in cubes(b):
            assert grid[x][y][z] == id_, (x, y, z)
            grid[x][y][z] = -1

    def place(b, id_):
        for x, y, z in cubes(b):
            assert grid[x][y][z] == -1, (x, y, z)
            grid[x][y][z] = id_

    def move_down(b, id_):
        bd = coords_down(b)
        if not can_place(bd, id_):
            return None

        clear(b, id_)
        place(bd, id_)
        return bd

    bricks.sort(key=lambda b: b[0][2])

    for id_ in xrange(0, len(bricks)):
        place(bricks[id_], id_)

        while True:
            bd = move_down(bricks[id_], id_)
            if bd is not None:
                bricks[id_] = bd
            else:
                break

    def supported_by(id_):
        return set(filter(lambda v: v not in (-1, id_), map(lambda (x, y, z): grid[x][y][z-1], cubes(bricks[id_]))))

    by = dict()
    for id_ in xrange(0, len(bricks)):
        by[id_] = supported_by(id_)

    supports = defaultdict(list)
    for id_ in by.keys():
        for bid_ in by[id_]:
            supports[bid_].append(id_)

    def dfs(id_, destroyed):
        destroyed.add(id_)

        todo = set()
        for sid in supports[id_]:
            if all(bid in destroyed for bid in by[sid]):
                todo.add(sid)
                destroyed.add(sid)

        for id_ in todo:
            dfs(id_, destroyed)

        return len(destroyed) - 1

    return sum(dfs(id_, set()) for id_ in xrange(0, len(bricks)))


def parse(input):
    return map(
        lambda s: tuple(tuple(map(int, t.split(","))) for t in s.split("~")),
        input.splitlines()
    )


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
