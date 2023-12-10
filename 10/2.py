def solution(sketch):

    start = [(i, j) for i in xrange(0, len(sketch)) for j in xrange(0, len(sketch[i])) if sketch[i][j] == "S"][0]

    move = lambda p, d: (p[0] + d[0], p[1] + d[1])
    is_legal = lambda p: 0 <= p[0] < len(sketch) and 0 <= p[1] < len(sketch[0])
    get_p = lambda p: sketch[p[0]][p[1]]

    def set_p(p, ch):
        sketch[p[0]][p[1]] = ch

    def bfs(q, seen, forbidden, cb=None):
        lefts = "FL-"
        if len(forbidden) > 0:
            lefts += "S"

        rights = "J7-"
        if len(forbidden) > 0:
            rights += "S"

        ups = "7F|"
        if len(forbidden) > 0:
            ups += "S"

        downs = "|JL"
        if len(forbidden) > 0:
            downs += "S"

        while len(q) > 0:
            q2 = []

            for p in q:
                pl = move(p, (0, -1))
                if get_p(p) in "S-J7" and pl not in seen and is_legal(pl) and get_p(pl) in lefts and pl not in forbidden:
                    seen.add(pl)
                    q2.append(pl)
                    if cb is not None:
                        cb(pl, "left")

                pr = move(p, (0, 1))
                if get_p(p) in "S-FL" and pr not in seen and is_legal(pr) and get_p(pr) in rights and pr not in forbidden:
                    seen.add(pr)
                    q2.append(pr)
                    if cb is not None:
                        cb(pr, "right")

                pu = move(p, (-1, 0))
                if get_p(p) in "S|LJ" and pu not in seen and is_legal(pu) and get_p(pu) in ups and pu not in forbidden:
                    seen.add(pu)
                    q2.append(pu)
                    if cb is not None:
                        cb(pu, "up")

                pd = move(p, (1, 0))
                if get_p(p) in "S|F7" and pd not in seen and is_legal(pd) and get_p(pd) in downs and pd not in forbidden:
                    seen.add(pd)
                    q2.append(pd)
                    if cb is not None:
                        cb(pd, "down")

            assert len(forbidden) == 0 or len(q2) <= 1

            q = q2

    q, seen, forbidden = [start], set([start]), set()
    bfs(q, seen, forbidden)

    def dfs(n):
        stack = [n]
        while len(stack) > 0:
            n = stack.pop()
            if not is_legal(n) or n in seen or get_p(n) == "0":
                continue
            set_p(n, "0")
            for d in ((di, dj) for di in xrange(-1, 2) for dj in xrange(-1, 2) if not (di == 0 and dj == 0)):
                stack.append(move(n, d))

    # starting from the bounds, fill all non-loop tiles/pipes

    for i in xrange(0, len(sketch)):
        dfs((i, 0))
        dfs((i, len(sketch[i])-1))
    for j in xrange(0, len(sketch[0])):
        dfs((0, j))
        dfs((len(sketch)-1, j))

    # find loop node that has out tile nearby
    start2, out_pos = None, None
    for n in seen:
        if get_p(n) not in "|-":
            continue

        nu = move(n, (-1, 0))
        if is_legal(nu) and get_p(nu) == "0" and start2 is None:
            start2 = n
            out_pos = "up"
            break

        nd = move(n, (1, 0))
        if is_legal(nd) and get_p(nd) == "0" and start2 is None:
            start2 = n
            out_pos = "down"
            break

        nl = move(n, (0, -1))
        if is_legal(nl) and get_p(nl) == "0" and start2 is None:
            start2 = n
            out_pos = "left"
            break

        nr = move(n, (0, 1))
        if is_legal(nr) and get_p(nr) == "0" and start2 is None:
            start2 = n
            out_pos = "right"
            break

    assert start2 is not None

    start3 = None
    if get_p(start2) == "|":
        if out_pos == "left":
            start3 = move(start2, (-1, 0))
        else:
            start3 = move(start2, (1, 0))
    elif get_p(start2) == "-":
        if out_pos == "up":
            start3 = move(start2, (0, 1))
        else:
            start3 = move(start2, (0, -1))

    assert start3 in seen

    q2, seen2, forbidden2 = [start3], set([start3]), set([start2])

    outs = []

    def fill_outs(p, d):
        if get_p(p) == "-":
            if d == "left":
                outs.append(move(p, (1, 0)))
            elif d == "right":
                outs.append(move(p, (-1, 0)))
        if get_p(p) == "|":
            if d == "up":
                outs.append(move(p, (0, -1)))
            elif d == "down":
                outs.append(move(p, (0, 1)))
        if get_p(p) == "L":
            if d == "left":
                outs.append(move(p, (0, -1)))
                outs.append(move(p, (1, -1)))
                outs.append(move(p, (1, 0)))
            elif d == "down":
                outs.append(move(p, (-1, 1)))
        if get_p(p) == "J":
            if d == "right":
                outs.append(move(p, (-1, -1)))
            if d == "down":
                outs.append(move(p, (0, 1)))
                outs.append(move(p, (1, 0)))
                outs.append(move(p, (1, 1)))
        if get_p(p) == "7":
            if d == "right":
                outs.append(move(p, (-1, 0)))
                outs.append(move(p, (-1, 1)))
                outs.append(move(p, (0, 1)))
            elif d == "up":
                outs.append(move(p, (1, -1)))
        if get_p(p) == "F":
            if d == "left":
                outs.append(move(p, (1, 1)))
            if d == "up":
                outs.append(move(p, (-1, -1)))
                outs.append(move(p, (-1, 0)))
                outs.append(move(p, (0, -1)))

    bfs(q2, seen2, forbidden2, fill_outs)

    outs = filter(lambda p: p not in seen and get_p(p) != "0", filter(is_legal, outs))

    for p in outs:
        dfs(p)

    return len([(i, j) for i in xrange(0, len(sketch)) for j in xrange(0, len(sketch[i])) if get_p((i, j)) != "0" and (i, j) not in seen])


def parse(input):
    return map(list, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
