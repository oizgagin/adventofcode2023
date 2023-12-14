def solution(platform):

    def pprint():
        print "\n".join(map(lambda s: "".join(s), platform))
        print

    def tilt_up():
        def tilt_up_col(col):
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
            tilt_up_col(j)

    def tilt_down():
        def tilt_down_col(col):
            s, c = len(platform), 0
            for row in xrange(len(platform)-1, -1, -1):
                if platform[row][col] == ".":
                    continue
                elif platform[row][col] == "O":
                    c += 1
                elif platform[row][col] == "#":
                    for i in xrange(0, c):
                        platform[s-1-i][col] = "O"
                    for i in xrange(s-1-c, row, -1):
                        platform[i][col] = "."
                    s, c = row, 0

            if c != 0:
                for i in xrange(0, c):
                    platform[s-1-i][col] = "O"
                for i in xrange(s-1-c, -1, -1):
                    platform[i][col] = "."

        for j in xrange(0, len(platform[0])):
            tilt_down_col(j)

    def tilt_left():
        def tilt_left_row(row):
            s, c = -1, 0
            for col in xrange(0, len(platform[row])):
                if platform[row][col] == ".":
                    continue
                elif platform[row][col] == "O":
                    c += 1
                elif platform[row][col] == "#":
                    for j in xrange(0, c):
                        platform[row][s+1+j] = "O"
                    for j in xrange(s+1+c, col):
                        platform[row][j] = "."
                    s, c = col, 0

            if c != 0:
                for j in xrange(0, c):
                    platform[row][s+1+j] = "O"
                for j in xrange(s+1+c, len(platform[0])):
                    platform[row][j] = "."

        for i in xrange(0, len(platform[0])):
            tilt_left_row(i)

    def tilt_right():
        def tilt_right_row(row):
            s, c = len(platform[row]), 0
            for col in xrange(len(platform[row])-1, -1, -1):
                if platform[row][col] == ".":
                    continue
                elif platform[row][col] == "O":
                    c += 1
                elif platform[row][col] == "#":
                    for j in xrange(0, c):
                        platform[row][s-1-j] = "O"
                    for j in xrange(s-1-c, col, -1):
                        platform[row][j] = "."
                    s, c = col, 0

            if c != 0:
                for j in xrange(0, c):
                    platform[row][s-1-j] = "O"
                for j in xrange(s-1-c, -1, -1):
                    platform[row][j] = "."

        for i in xrange(0, len(platform)):
            tilt_right_row(i)

    def count(ch):
        c = 0
        for i in xrange(0, len(platform)):
            for j in xrange(0, len(platform[i])):
                if platform[i][j] == ch:
                    c += 1
        return c

    def cycle():
        tilt_up()
        tilt_left()
        tilt_down()
        tilt_right()

    def hash_():
        return int("".join(map("".join, platform)).replace(".", "0").replace("#", "1").replace("O", "2"), 3)

    def load():
        sum_ = 0
        for i in xrange(0, len(platform)):
            for j in xrange(0, len(platform[i])):
                if platform[i][j] == "O":
                    sum_ += len(platform) - i
        return sum_

    memo = {
        hash_(): 0,
    }

    cycles = 1000000000

    steps, period_len = 0, 0
    while True:
        cycle()
        steps += 1

        h = hash_()

        if h in memo:
            period_len = steps - memo[h]
            for i in xrange(0, (cycles - memo[h]) % period_len):
                cycle()
            return load()
        else:
            memo[h] = steps


def parse(input):
    return map(list, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
