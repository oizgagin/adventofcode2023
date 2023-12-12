import multiprocessing


def check(pattern, rec):
    for i in xrange(0, len(pattern)):
        if pattern[i] == "#" and rec[i] != "#":
            return False
        if pattern[i] == "." and rec[i] != ".":
            return False
    return True


def generate(t):
    pattern, groups = t
    memo = {}

    def generate_all(pattern, groups):
        cap = len(pattern)

        if len(groups) == 0:
            return 1

        if len(groups) == 1:
            return len(filter(
                lambda s: check(pattern, s),
                [("." * i + "#" * groups[0] + "." * (cap - groups[0] - i)) for i in xrange(0, cap - groups[0] + 1)]
            ))

        if cap < sum(groups) + len(groups) - 1:
            return 0

        if (cap, groups) in memo:
            return memo[(cap, groups)]

        res = 0
        for i in xrange(0, cap):
            pref = "." * i + "#" * groups[0] + "."
            if len(pref) > cap:
                break

            if not check(pattern[:len(pref)], pref):
                continue

            res += generate_all(pattern[len(pref):], groups[1:])

        memo[(cap, groups)] = res
        return memo[(cap, groups)]

    return generate_all(pattern, groups)


def solution(records):
    pool = multiprocessing.Pool(processes=8)
    records = map(lambda rec: ("?".join([rec[0]] * 5), rec[1] * 5), records)
    return sum(pool.imap_unordered(generate, records))


def parse(input):
    return map(lambda s: (s.split()[0], tuple(map(int, s.split()[1].split(",")))), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
