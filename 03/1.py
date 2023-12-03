import string, collections


def solution(schematic):
    grid = collections.defaultdict(lambda: collections.defaultdict(lambda: "."))
    for i, line in enumerate(schematic):
        for j, ch in enumerate(line):
            grid[i][j] = ch

    ds = [(di, dj) for di in xrange(-1, 2) for dj in xrange(-1, 2) if not (di == 0 and dj == 0)]

    is_symbol = lambda ch: ch not in "." + string.digits

    i, j, sum_ = 0, 0, 0
    while True:
        if i == len(schematic):
            break

        if j == len(schematic[i]):
            i, j = i+1, 0
            continue

        if is_symbol(grid[i][j]):
            j += 1
            continue

        if grid[i][j] == ".":
            j += 1
            continue

        assert str.isdigit(grid[i][j])

        for di, dj in ds:
            if is_symbol(grid[i+di][j+dj]):
                l = j
                while str.isdigit(grid[i][l]):
                    l -= 1

                r = j
                while str.isdigit(grid[i][r]):
                    r += 1

                sum_ += int(schematic[i][l+1:r])

                j = r
                break
        else:
            j += 1
            continue

    return sum_


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
