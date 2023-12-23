from collections import defaultdict
import heapq
import sys

sys.setrecursionlimit(100 * 1000)


def solution(map_):
    start = [(0, j) for j in xrange(0, len(map_[0])) if map_[0][j] == "."][0]
    end = [(len(map_)-1, j) for j in xrange(0, len(map_[0])) if map_[len(map_)-1][j] == "."][0]

    dists = defaultdict(lambda: float("-inf"))

    def dfs(p, d, seen=set()):
        dists[p] = max(dists[p], d)

        i, j = p

        next_ = []
        if map_[i][j] == ">":
            next_.append((i, j+1))
        elif map_[i][j] == "<":
            next_.append((i, j-1))
        elif map_[i][j] == "v":
            next_.append((i+1, j))
        else:
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if 0 <= i+di < len(map_) and 0 <= j+dj < len(map_[i+di]) and map_[i+di][j+dj] != "#":
                    next_.append((i+di, j+dj))

        for pn in next_:
            if pn not in seen:
                seen.add(pn)
                dfs(pn, d+1, seen)
                seen.remove(pn)

    dfs(start, 0)
    return abs(dists[end])


def parse(input):
    return map(list, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
