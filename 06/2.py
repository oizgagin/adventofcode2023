def solution(times, distances):
    time = int(''.join(map(str, times)))
    dist = int(''.join(map(str, distances)))

    c = 0
    for speed in xrange(0, time):
        if speed * (time - speed) > dist:
            c += 1
    return c


def parse(input):
    return tuple(map(lambda s: map(int, s.split()[1:]), input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
