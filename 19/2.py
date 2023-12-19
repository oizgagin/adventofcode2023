def solution(workflows, parts):
    accepted = []

    def eval_(w, x, m, a, s):
        if w == "A":
            accepted.append((x, m, a, s))
            return

        if w == "R":
            return

        for r in workflows[w]:
            if r[0] == "NOOP":
                eval_(r[1], x, m, a, s)
            else:
                cmp, rating, threshold, next_ = r

                b = {
                    "x": x,
                    "m": m,
                    "a": a,
                    "s": s,
                }

                if cmp == ">":
                    if threshold >= b[rating][1]:
                        continue

                    if b[rating][0] < threshold < b[rating][1]:
                        b[rating] = (threshold+1, b[rating][1])
                else:
                    if threshold <= b[rating][0]:
                        continue

                    if b[rating][0] < threshold < b[rating][1]:
                        b[rating] = (b[rating][0], threshold-1)

                eval_(next_, b["x"], b["m"], b["a"], b["s"])

                b = {
                    "x": x,
                    "m": m,
                    "a": a,
                    "s": s,
                }

                if cmp == ">":
                    if b[rating][0] < threshold < b[rating][1]:
                        b[rating] = (b[rating][0], threshold)
                    else:
                        b[rating] = (1, threshold)
                else:
                    if b[rating][0] < threshold < b[rating][1]:
                        b[rating] = (threshold, b[rating][1])
                    else:
                        b[rating] = (threshold, 4000)

                x, m, a, s = b["x"], b["m"], b["a"], b["s"]

    eval_("in", (1, 4000), (1, 4000), (1, 4000), (1, 4000))

    sum_ = 0
    for x, m, a, s in accepted:
        sum_ += (
            (x[1] - x[0] + 1) *
            (m[1] - m[0] + 1) *
            (a[1] - a[0] + 1) *
            (s[1] - s[0] + 1)
        )

    return sum_


def parse(input):

    def parse_rules(line):
        res = []
        for rule in line.split(","):
            if ":" not in rule:
                res.append(("NOOP", rule))
            else:
                cmp, next_ = tuple(rule.split(":"))
                res.append((cmp[1], cmp[0], int(cmp[2:]), next_))
        return res

    def parse_workflow(line):
        id_, rules = tuple(line.split("{"))
        return (id_, parse_rules(rules.strip("}")))

    def parse_part(line):
        res = {}
        for s in line.strip("{}").split(","):
            res[s[0]] = int(s[2:])
        return res

    workflows, parts = input.split("\n\n")

    return dict(map(parse_workflow, workflows.splitlines())), map(parse_part, parts.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
