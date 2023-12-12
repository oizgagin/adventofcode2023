def solution(records):

    def check(s, g):
        c, ig, in_ = 0, 0, False

        for ch in s:
            if ch == "." and in_:
                if ig >= len(g) or c != g[ig]: return False
                c, ig, in_ = 0, ig + 1, False
            elif ch == "#":
                c, in_ = c + 1, True

        return ig == len(g)-1 and c == g[ig] if in_ else ig == len(g)

    def recurse(rec, i, group):
        if i == len(rec):
            return 1 if check(rec, group) else 0

        if rec[i] == "." or rec[i] == "#":
            return recurse(rec, i+1, group)

        assert rec[i] == "?"

        c = 0

        rec[i] = "."
        c += recurse(rec, i+1, group)

        rec[i] = "#"
        c += recurse(rec, i+1, group)

        rec[i] = "?"

        return c

    return sum(recurse(rec, 0, group) for rec, group in records)


def parse(input):
    return map(lambda s: (list(s.split()[0]), tuple(map(int, s.split()[1].split(",")))), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
