def solution(cards):
    wins = map(lambda card: len([n for n in card[1] if n in card[0]]), cards)

    amounts = [1] * len(cards)

    for i in xrange(0, len(cards)):
        for j in xrange(0, wins[i]):
            amounts[i+j+1] += amounts[i]

    return sum(amounts)


def parse(input):
    return map(lambda line: tuple(map(lambda nums: tuple(map(int, nums.split())), line.split(":")[1].split("|"))), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
