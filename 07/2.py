import collections


def solution(hands):

    card2strength = dict(
        [(str(digit), digit) for digit in xrange(2, 10)] +
        [(card, strength) for (strength, card) in enumerate("TQKA", 10)] +
        [("J", 1)]
    )

    cards = filter(lambda c: c != "J", list(card2strength))

    hand_types = {
        "HIGH_CARD": 1,
        "ONE_PAIR": 2,
        "TWO_PAIR": 3,
        "THREE_OF_A_KIND": 4,
        "FULL_HOUSE": 5,
        "FOUR_OF_A_KIND": 6,
        "FIVE_OF_A_KIND": 7,
    }

    def hand_type(hand):
        c = collections.Counter(hand)

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

        assert len(filter(lambda v: v == 2, c.values())) == 1, (hand, c.values())
        return "ONE_PAIR"

    memo = {}

    def hand_type_j(hand_j):
        if "J" not in hand_j:
            return hand_type(hand_j)

        if hand_j in memo:
            return memo[hand_j]

        hand_p = filter(lambda c: c != "J", hand_j)

        max_ = "HIGH_CARD"
        for i in xrange(0, len(cards) ** (len(hand_j) - len(hand_p))):
            hand = hand_p

            j = i
            for _ in xrange(0, len(hand_j) - len(hand_p)):
                hand += cards[j % len(cards)]
                j /= len(cards)

            type_ = hand_type(hand)
            if hand_types[type_] > hand_types[max_]:
                max_ = type_

        memo[hand_j] = max_
        return max_

    def cmp_hands(hand1, hand2):
        t1, t2 = hand_type_j(hand1), hand_type_j(hand2)
        if t1 != t2:
            return -1 if hand_types[t1] < hand_types[t2] else +1

        for i in xrange(0, len(hand1)):
            if card2strength[hand1[i]] == card2strength[hand2[i]]:
                continue
            return -1 if card2strength[hand1[i]] < card2strength[hand2[i]] else +1

        raise Exception("unreachable")

    sum_ = 0
    for rank, (hand, bid) in enumerate(sorted(hands, cmp=lambda cr1, cr2: cmp_hands(cr1[0], cr2[0])), 1):
        print rank, hand, bid
        sum_ += rank * bid
    return sum_


def parse(input):
    return map(lambda s: (s.split()[0], int(s.split()[1])), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
