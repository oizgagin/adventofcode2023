def solution(image):
    expand_rows = filter(lambda i: all(image[i][j] == "." for j in xrange(0, len(image[i]))), xrange(0, len(image)))
    expand_cols = filter(lambda j: all(image[i][j] == "." for i in xrange(0, len(image))), xrange(0, len(image[0])))

    galaxies = [(i, j) for i in xrange(0, len(image)) for j in xrange(0, len(image[i])) if image[i][j] == "#"]

    sum_ = 0
    for i in xrange(0, len(galaxies)):
        for j in xrange(i+1, len(galaxies)):
            gi, gj = galaxies[i], galaxies[j]

            d = abs(gi[0] - gj[0]) + abs(gi[1] - gj[1])
            for c in expand_cols:
                if min(gi[1], gj[1]) < c < max(gi[1], gj[1]):
                    d += (1000000 - 1)
            for r in expand_rows:
                if min(gi[0], gj[0]) < r < max(gi[0], gj[0]):
                    d += (1000000 - 1)

            sum_ += d

    return sum_


def parse(input):
    return map(list, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
