import collections


def solution(sequence):

    def hash_(s):
        h = 0
        for ch in s:
            h += ord(ch)
            h *= 17
            h %= 256
        return h

    boxes = collections.defaultdict(list)

    for op in sequence:

        if "-" in op:
            label = op.strip("-")
            box = hash_(label)
            for i, lens in enumerate(boxes[box]):
                if lens[0] == label:
                    boxes[box].pop(i)
                    break

        if "=" in op:
            label, focal = tuple(op.split("="))
            box = hash_(label)
            focal = int(focal)

            for i, lens in enumerate(boxes[box]):
                if lens[0] == label:
                    lens[1] = focal
                    break
            else:
                boxes[box].append([label, focal])

    sum_ = 0
    for box, lenses in boxes.iteritems():
        for i, lens in enumerate(lenses, 1):
            sum_ += (box + 1) * i * lens[1]
    return sum_


def parse(input):
    return input.strip().split(",")


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()