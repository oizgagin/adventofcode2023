import collections
import heapq


def solution(map_):
    is_legal = lambda p: 0 <= p[0] < len(map_) and 0 <= p[1] < len(map_[p[0]])
    move = lambda p, d: (p[0] + d[0], p[1] + d[1])
    get_p = lambda p: map_[p[0]][p[1]]

    dists = collections.defaultdict(lambda: float("+inf"))
    start = (0, (0, 0), 10, 0, 10, 0)

    pq, seen = [start], set()
    while len(pq) > 0:
        loss, p, ups, downs, lefts, rights = heapq.heappop(pq)

        dists[p] = min(dists[p], loss)

        if ups < 10:
            if ups == 0:
                ud = 4
            else:
                ud = 1

            up = move(p, (-ud, 0))

            if is_legal(up):
                k = (up, ups + ud, 10, 0, 0)
                if k not in seen:
                    seen.add(k)
                    uploss = sum(get_p(move(p, (-di, 0))) for di in xrange(1, ud+1))
                    heapq.heappush(pq, (loss + uploss,) + k)

        if downs < 10:
            if downs == 0:
                dd = 4
            else:
                dd = 1

            down = move(p, (dd, 0))

            if is_legal(down):
                k = (down, 10, downs + dd, 0, 0)
                if k not in seen:
                    seen.add(k)
                    downloss = sum(get_p(move(p, (di, 0))) for di in xrange(1, dd+1))
                    heapq.heappush(pq, (loss + downloss,) + k)

        if lefts < 10:
            if lefts == 0:
                ld = 4
            else:
                ld = 1

            left = move(p, (0, -1 * ld))

            if is_legal(left):
                k = (left, 0, 0, lefts + ld, 10)
                if k not in seen:
                    seen.add(k)
                    leftloss = sum(get_p(move(p, (0, -dj))) for dj in xrange(1, ld+1))
                    heapq.heappush(pq, (loss + leftloss,) + k)

        if rights < 10:
            if rights == 0:
                rd = 4
            else:
                rd = 1

            right = move(p, (0, 1 * rd))

            if is_legal(right):
                k = (right, 0, 0, 10, rights + rd)
                if k not in seen:
                    seen.add(k)
                    rightloss = sum(get_p(move(p, (0, dj))) for dj in xrange(1, rd+1))
                    heapq.heappush(pq, (loss + rightloss,) + k)

    return dists[(len(map_)-1, len(map_[0])-1)]


def parse(input):
    return map(lambda s: map(int, list(s)), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
