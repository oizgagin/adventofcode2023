import collections
import heapq


def solution(map_):
    is_legal = lambda p: 0 <= p[0] < len(map_) and 0 <= p[1] < len(map_[p[0]])
    move = lambda p, d: (p[0] + d[0], p[1] + d[1])
    get_p = lambda p: map_[p[0]][p[1]]

    dists = collections.defaultdict(lambda: float("+inf"))
    start = (0, (0, 0), 0, 3, 0, 3)

    pq, seen = [start], set()
    while len(pq) > 0:
        loss, p, ups, downs, lefts, rights = heapq.heappop(pq)

        dists[p] = min(dists[p], loss)

        if ups > 0:
            up = move(p, (-1, 0))
            if is_legal(up):
                k = (up, ups-1, 0, 3, 3)
                if k not in seen:
                    seen.add(k)
                    heapq.heappush(pq, (loss + get_p(up),) + k)

        if downs > 0:
            down = move(p, (1, 0))
            if is_legal(down):
                k = (down, 0, downs-1, 3, 3)
                if k not in seen:
                    seen.add(k)
                    heapq.heappush(pq, (loss + get_p(down),) + k)

        if lefts > 0:
            left = move(p, (0, -1))
            if is_legal(left):
                k = (left, 3, 3, lefts-1, 0)
                if k not in seen:
                    seen.add(k)
                    heapq.heappush(pq, (loss + get_p(left),) + k)

        if rights > 0:
            right = move(p, (0, 1))
            if is_legal(right):
                k = (right, 3, 3, 0, rights-1)
                if k not in seen:
                    seen.add(k)
                    heapq.heappush(pq, (loss + get_p(right),) + k)

    return dists[(len(map_)-1, len(map_[0])-1)]


def parse(input):
    return map(lambda s: map(int, list(s)), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
