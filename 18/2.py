def solution(plan):
    p = (0, 0)
    points = []

    dirs = {"0": "R", "1": "D", "2": "L", "3": "U"}
    P = 0

    for _, _, rgb in plan:
        rgb = rgb.strip("#()")
        dir_, d = dirs[rgb[-1]], int(rgb[:-1], 16)
        P += d
        if dir_ == "U":
            p = (p[0], p[1] + d)
        elif dir_ == "D":
            p = (p[0], p[1] - d)
        elif dir_ == "L":
            p = (p[0]-d, p[1])
        else:
            p = (p[0]+d, p[1])
        points.append(p)

    a = abs(sum(points[i-1][0] * points[i][1] - points[i][0] * points[i-1][1] for i in xrange(1, len(points))) / 2)

    return a + P / 2 + 1


def parse(input):
    def f(line):
        dir_, d, rgb = tuple(line.split())
        return (dir_, int(d), rgb)

    return map(f, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()