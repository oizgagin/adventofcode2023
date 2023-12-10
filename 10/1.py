def solution(sketch):
    start = [(i, j) for i in xrange(0, len(sketch)) for j in xrange(0, len(sketch[i])) if sketch[i][j] == "S"][0]

    move = lambda p, d: (p[0] + d[0], p[1] + d[1])
    is_legal = lambda p: 0 <= p[0] < len(sketch) and 0 <= p[1] < len(sketch[0])
    get_p = lambda p: sketch[p[0]][p[1]]

    q = [start]
    seen = set([start])
    steps = 0

    while len(q) > 0:
        q2 = []

        for p in q:
            pl = move(p, (0, -1))
            if get_p(p) in "S-J7" and pl not in seen and is_legal(pl) and get_p(pl) in "FL-":
                seen.add(pl)
                q2.append(pl)

            pr = move(p, (0, 1))
            if get_p(p) in "S-FL" and pr not in seen and is_legal(pr) and get_p(pr) in "J7-":
                seen.add(pr)
                q2.append(pr)

            pu = move(p, (-1, 0))
            if get_p(p) in "S|LJ" and pu not in seen and is_legal(pu) and get_p(pu) in "7F|":
                seen.add(pu)
                q2.append(pu)

            pd = move(p, (1, 0))
            if get_p(p) in "S|F7" and pd not in seen and is_legal(pd) and get_p(pd) in "|JL":
                seen.add(pd)
                q2.append(pd)

        if len(q2) == 0:
            return steps

        steps += 1
        q = q2


def parse(input):
    return map(list, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
