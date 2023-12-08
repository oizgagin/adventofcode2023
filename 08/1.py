def solution(instrs, nodes):
    curr_i, curr_node, steps = 0, "AAA", 0

    while True:
        if curr_i >= len(instrs):
            curr_i = 0

        steps += 1

        curr_node = nodes[curr_node][instrs[curr_i]]
        if curr_node == "ZZZ":
            return steps

        curr_i += 1


def parse(input):
    instrs = map(lambda i: 0 if i == "L" else 1, input.splitlines()[0])

    nodes = dict()
    for line in input.splitlines()[2:]:
        nodes[line.split()[0]] = tuple(map(lambda s: s.strip("(),"), line.split()[2:]))
    return instrs, nodes


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
