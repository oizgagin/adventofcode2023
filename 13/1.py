def solution(patterns):

    def s2i(s):
        return int(s.replace(".", "0").replace("#", "1"), 2)

    def getcol(pattern, j):
        return "".join([pattern[i][j] for i in xrange(0, len(pattern))])

    def rows(pattern):
        return map(s2i, pattern)

    def cols(pattern):
        return map(s2i, [getcol(pattern, j) for j in xrange(0, len(pattern[0]))])

    def symmetries(arr):
        for i in xrange(0, len(arr)-1):
            if arr[i] == arr[i+1]:
                j = 1
                while i-j >= 0 and i+1+j < len(arr):
                    if arr[i-j] != arr[i+1+j]:
                        break
                    j += 1
                else:
                    return i+1

        return 0

    return sum(100 * symmetries(rows(pattern)) + symmetries(cols(pattern)) for pattern in patterns)


def parse(input):
    return map(lambda b: b.splitlines(), input.split("\n\n"))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
