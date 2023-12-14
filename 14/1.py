def solution(platform):

    def pprint():
        print "\n".join(map(lambda s: "".join(s), platform))
        print

    def tilt_up(col):
        s, c = -1, 0
        for row in xrange(0, len(platform)):
            if platform[row][col] == ".":
                continue
            elif platform[row][col] == "O":
                c += 1
            elif platform[row][col] == "#":
                for i in xrange(0, c):
                    platform[s+1+i][col] = "O"
                for i in xrange(s+1+c, row):
                    platform[i][col] = "."
                s, c = row, 0

        if c != 0:
            for i in xrange(0, c):
                platform[s+1+i][col] = "O"
            for i in xrange(s+1+c, len(platform)):
                platform[i][col] = "."

    for j in xrange(0, len(platform[0])):
        tilt_up(j)

    sum_ = 0
    for i in xrange(0, len(platform)):
        for j in xrange(0, len(platform[i])):
            if platform[i][j] == "O":
                sum_ += len(platform) - i
    return sum_


def parse(input):
    return map(list, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()