import fractions


def solution(instrs, nodes):

    def find_period(node):
        curr_i, curr_node, steps = 0, node, 0

        while True:
            curr_node = nodes[curr_node][instrs[curr_i]]
            curr_i = (curr_i + 1) % len(instrs)
            steps += 1

            if curr_node.endswith("Z"):
                return steps

    periods = []
    for node in filter(lambda node: node.endswith("A"), nodes):
        periods.append(find_period(node))

    gcd = lambda l: reduce(lambda acc, x: fractions.gcd(acc, x), l, l[0])
    prod = lambda it: reduce(lambda acc, x: acc * x, it, 1)

    return gcd(periods) * prod(map(lambda p: p / gcd(periods), periods))


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
