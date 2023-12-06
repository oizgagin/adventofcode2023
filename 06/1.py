def solution(times, distances):
    res = 1

    for i in xrange(0, len(times)):
        c = 0
        for speed in xrange(0, times[i]):
            if speed * (times[i] - speed) > distances[i]:
                c += 1
        res *= c

    return res


def parse(input):
    return tuple(map(lambda s: map(int, s.split()[1:]), input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
