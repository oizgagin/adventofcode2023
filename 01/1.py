def solution(calibrations):

    def d(s):
        for ch in s:
            if ch.isdigit():
                return ch

    return sum(int(d(cal) + d(cal[::-1])) for cal in calibrations)


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
