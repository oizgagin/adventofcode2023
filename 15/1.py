def solution(sequence):

    def hash_(s):
        h = 0
        for ch in s:
            h += ord(ch)
            h *= 17
            h %= 256
        return h

    return sum(map(hash_, sequence))


def parse(input):
    return input.strip().split(",")


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()