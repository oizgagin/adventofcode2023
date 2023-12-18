import collections


def solution(plan):
    grid = collections.defaultdict(lambda: False)

    ds = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    move = lambda p, d: (p[0] + d[0], p[1] + d[1])
    mul = lambda p, x: (p[0] * x, p[1] * x)

    curr = (0, 0)
    grid[curr] = True

    for dir_, d, _ in plan:
        for i in xrange(1, d+1):
            grid[move(curr, mul(ds[dir_], i))] = True
        curr = move(curr, mul(ds[dir_], d))

    is_, js = map(lambda p: p[0], grid.keys()), map(lambda p: p[1], grid.keys())
    mini, maxi, minj, maxj = min(is_), max(is_), min(js), max(js)

    inner = None

    for i in xrange(mini, maxi+1):
        for j in xrange(minj, maxj+1):
            if grid[(i, j)]: continue

            c = 0
            for jj in xrange(j+1, maxj+1):
                if grid[(i, jj)]:
                    c += 1

            if c % 2 != 0:
                inner = (i, j)
                break

    assert inner is not None

    def dfs(start):
        stack = []
        stack.append(start)

        while len(stack) > 0:
            c = stack.pop()
            if grid[c]:
                continue
            if not (mini <= c[0] <= maxi and minj <= c[1] <= maxj):
                continue
            grid[c] = True
            for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                dc = move(c, d)
                if grid[dc]:
                    continue
                if not (mini <= dc[0] <= maxi and minj <= dc[1] <= maxj):
                    continue
                stack.append(dc)

    dfs(inner)

    return len(filter(None, grid.values()))


def parse(input):
    def f(line):
        dir_, d, rgb = tuple(line.split())
        return (dir_, int(d), rgb)

    return map(f, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()