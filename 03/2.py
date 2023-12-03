import string, collections


def solution(schematic):
    id_ = 0

    grid = collections.defaultdict(lambda: collections.defaultdict(lambda: (None, ".")))
    for i, line in enumerate(schematic):
        currid = None

        for j, ch in enumerate(line):
            if str.isdigit(ch):
                if currid is None:
                    currid = id_
                    id_ += 1
            else:
                currid = None

            grid[i][j] = (currid, ch)

    ds = [(di, dj) for di in xrange(-1, 2) for dj in xrange(-1, 2) if not (di == 0 and dj == 0)]

    def extract_num(coord):
        i, j = coord

        l = j
        while str.isdigit(grid[i][l][1]):
            l -= 1
        r = j
        while str.isdigit(grid[i][r][1]):
            r += 1
        return int(schematic[i][l+1:r])

    i, j, sum_ = 0, 0, 0
    while True:
        if i == len(schematic):
            break

        if j == len(schematic[i]):
            i, j = i+1, 0
            continue

        if grid[i][j][1] != "*":
            j += 1
            continue

        seen_ids, coords = set(), []
        for di, dj in ds:
            id_, ch = grid[i+di][j+dj]

            if str.isdigit(ch) and id_ not in seen_ids:
                coords.append((i+di, j+dj))
                seen_ids.add(id_)

        if len(seen_ids) == 2:
            sum_ += extract_num(coords[0]) * extract_num(coords[1])

        j += 1

    return sum_


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
