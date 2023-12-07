import collections


def solution(cards):

    card2strength = dict(
        [(str(digit), digit) for digit in xrange(2, 10)] +
        [(card, strength) for (strength, card) in enumerate("TJQKA", 10)]
    )

    card_types = {
        "HIGH_CARD": 1,
        "ONE_PAIR": 2,
        "TWO_PAIR": 3,
        "THREE_OF_A_KIND": 4,
        "FULL_HOUSE": 5,
        "FOUR_OF_A_KIND": 6,
        "FIVE_OF_A_KIND": 7,
    }

    def card_type(card):
        c = collections.Counter(card)

        if len(c) == 1:
            return "FIVE_OF_A_KIND"

        if len(c) == 5:
            return "HIGH_CARD"

        if any(v == 4 for v in c.values()):
            return "FOUR_OF_A_KIND"

        if any(v == 3 for v in c.values()):
            if any(v == 2 for v in c.values()):
                return "FULL_HOUSE"
            return "THREE_OF_A_KIND"

        if len(filter(lambda v: v == 2, c.values())) == 2:
            return "TWO_PAIR"

        assert len(filter(lambda v: v == 2, c.values())) == 1, (card, c.values())
        return "ONE_PAIR"

    def cmp_cards(card1, card2):
        t1, t2 = card_type(card1), card_type(card2)
        if t1 != t2:
            return -1 if card_types[t1] < card_types[t2] else +1

        for i in xrange(0, len(card1)):
            if card2strength[card1[i]] == card2strength[card2[i]]:
                continue
            return -1 if card2strength[card1[i]] < card2strength[card2[i]] else +1

        raise Exception("unreachable")

    sum_ = 0
    for rank, (card, bid) in enumerate(sorted(cards, cmp=lambda cr1, cr2: cmp_cards(cr1[0], cr2[0])), 1):
        print rank, card, bid
        sum_ += rank * bid
    return sum_


def parse(input):
    return map(lambda s: (s.split()[0], int(s.split()[1])), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
