def solution(map_):
    s = [(i, j) for i in xrange(0, len(map_)) for j in xrange(0, len(map_[i])) if map_[i][j] == "S"][0]
    map_[s[0]][s[1]] = "."

    def loop(q):
        s = set()

        for n in q:
            i, j = n
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if 0 <= i+di < len(map_) and 0 <= j+dj < len(map_[i]) and map_[i+di][j+dj] == ".":
                    s.add((i+di, j+dj))

        return s

    q = [s]
    for i in xrange(0, 64):
        q = loop(q)
    return len(q)


def parse(input):
    return map(list, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
