def solution(patterns):

    def s2i(s):
        return int(s.replace(".", "0").replace("#", "1"), 2)

    def getcol(pattern, j):
        return "".join([pattern[i][j] for i in xrange(0, len(pattern))])

    def rows(pattern):
        return map(s2i, pattern)

    def cols(pattern):
        return map(s2i, [getcol(pattern, j) for j in xrange(0, len(pattern[0]))])

    def count_ones(n):
        return bin(n).count("1")

    def symmetries(arr):
        res = 0

        for i in xrange(0, len(arr)-1):
            ones_used = False

            if arr[i] == arr[i+1] or count_ones(arr[i] ^ arr[i+1]) == 1:
                if arr[i] != arr[i+1]:
                    ones_used = True

                j = 1
                while i-j >= 0 and i+1+j < len(arr):
                    eq = arr[i-j] == arr[i+1+j]
                    if not eq and not ones_used:
                        if count_ones(arr[i-j] ^ arr[i+1+j]) == 1:
                            ones_used = True
                            eq = True

                    if not eq:
                        break

                    j += 1
                else:
                    if ones_used:
                        return i + 1

        return 0

    return sum(symmetries(rows(pattern)) * 100 + symmetries(cols(pattern)) for pattern in patterns)


def parse(input):
    return map(lambda b: b.splitlines(), input.split("\n\n"))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
