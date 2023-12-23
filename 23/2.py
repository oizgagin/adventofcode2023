from collections import defaultdict
import heapq
import sys

sys.setrecursionlimit(100 * 1000)

def solution(map_):
    start = [(0, j) for j in xrange(0, len(map_[0])) if map_[0][j] == "."][0]
    end = [(len(map_)-1, j) for j in xrange(0, len(map_[0])) if map_[len(map_)-1][j] == "."][0]

    add = lambda p, d: (p[0] + d[0], p[1] + d[1])
    dist = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    is_vert = lambda p1, p2: p1[1] == p2[1]
    is_hori = lambda p1, p2: p1[0] == p2[0]

    def intersect((p1, p2), (p3, p4)):
        if is_vert(p1, p2) and is_vert(p3, p4):
            return None
        if is_hori(p1, p2) and is_hori(p3, p4):
            return None

        v = (p1, p2) if is_vert(p1, p2) else (p3, p4)
        h = (p1, p2) if is_hori(p1, p2) else (p3, p4)

        vj, vi1, vi2 = v[0][1], min(v[0][0], v[1][0]), max(v[0][0], v[1][0])
        hi, hj1, hj2 = h[0][0], min(h[0][1], h[1][1]), max(h[0][1], h[1][1])

        if not (vi1 <= hi <= vi2 and hj1 <= vj <= hj2):
            return None

        return (hi, vj)

    for i in xrange(0, len(map_)):
        for j in xrange(0, len(map_[i])):
            if map_[i][j] in "><v": map_[i][j] = "."

    def down(i, j):
        map_[i][j] += "d"

        if i+1 >= len(map_):
            return None

        if map_[i+1][j] == "#":
            return None

        s = (i, j)
        while i < len(map_) and "#" not in map_[i][j]:
            map_[i][j] += "d"
            i += 1
        return (s, (i-1, j))

    def right(i, j):
        map_[i][j] += "r"

        if j+1 >= len(map_[i]):
            return None

        if map_[i][j+1] == "#":
            return None

        s = (i, j)
        while j < len(map_[i]) and "#" not in map_[i][j]:
            map_[i][j] += "r"
            j += 1
        return (s, (i, j-1))

    horis = []
    verts = []

    for i in xrange(0, len(map_)):
        for j in xrange(0, len(map_[i])):
            if "." in map_[i][j]:
                if "d" not in map_[i][j]:
                    d = down(i, j)
                    if d: verts.append(d)

                if "r" not in map_[i][j]:
                    r = right(i, j)
                    if r: horis.append(r)

    assert all(is_vert(*v) for v in verts)
    assert all(is_hori(*h) for h in horis)

    graph = defaultdict(set)

    for h1, h2 in horis:
        base = h1
        for v1, v2 in verts:
            ip = intersect((h1, h2), (v1, v2))
            if ip and ip not in (h1, h2):
                graph[base].add(ip)
                graph[ip].add(base)
                base = ip
        graph[base].add(h2)
        graph[h2].add(base)

    for v1, v2 in verts:
        base = v1
        for h1, h2 in horis:
            ip = intersect((h1, h2), (v1, v2))
            if ip and ip not in (v1, v2):
                graph[base].add(ip)
                graph[ip].add(base)
                base = ip
        graph[base].add(v2)
        graph[v2].add(base)

    assert start in graph
    assert end in graph

    assert all(len(graph[p]) > 1 for p in graph.keys() if p not in (start, end))

    for p in graph.keys():
        graph[p] = set(map(lambda n: (n, dist(n, p)), graph[p]))

    def compress(g):
        newg = defaultdict(set)

        for p in g.keys():
            newg[p] = set(list(g[p]))

        for p in g.keys():
            if len(g[p]) == 2:
                (s, sd), (e, ed) = tuple(g[p])

                newg[s].add((e, sd+ed))
                newg[s].remove((p, sd))

                newg[e].add((s, sd+ed))
                newg[e].remove((p, ed))

                del newg[p]
                return newg, True
        return newg, False

    while True:
        graph, compressed = compress(graph)
        if not compressed:
            break

    assert start in graph
    assert end in graph

    dists = defaultdict(lambda: float("-inf"))

    def dfs(p, d, seen=set()):
        dists[p] = max(dists[p], d)
        seen.add(p)

        if p == end:
            return

        for np, nd in graph[p]:
            if np not in seen:
                seen.add(np)
                dfs(np, d+nd, seen)
                seen.remove(np)

    dfs(start, 0)
    return dists[end]


def parse(input):
    return map(list, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
