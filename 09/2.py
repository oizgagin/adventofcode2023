def solution(histories):

    def predict(history):
        if all(v == 0 for v in history):
            return 0

        diffs = [history[i] - history[i-1] for i in xrange(1, len(history))]
        return history[0] - predict(diffs)

    return sum(predict(history) for history in histories)


def parse(input):
    return map(lambda s: map(int, s.split()), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
