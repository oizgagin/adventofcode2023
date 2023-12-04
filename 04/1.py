def solution(cards):
    sum_ = 0
    for card in cards:
        wins = len([n for n in card[1] if n in card[0]])
        if wins != 0:
            sum_ += 2 ** (wins-1)
    return sum_


def parse(input):
    return map(lambda line: tuple(map(lambda nums: tuple(map(int, nums.split())), line.split(":")[1].split("|"))), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
