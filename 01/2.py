def solution(calibrations):

    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    def d(s, rev=False):
        for i, ch in enumerate(s):
            if ch.isdigit():
                return ch

            for dd, dv in digits.iteritems():
                if s[i:i+len(dd)] == (dd if not rev else dd[::-1]):
                    return str(dv)

    return sum(int(d(cal) + d(cal[::-1], True)) for cal in calibrations)


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
