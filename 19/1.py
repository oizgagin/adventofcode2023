def solution(workflows, parts):

    cmps = {
        "<": (lambda x, y: x < y),
        ">": (lambda x, y: x > y),
    }

    def eval_(w, p):
        if w == "A":
            return True
        if w == "R":
            return False

        for r in workflows[w]:
            if r[0] == "NOOP":
                return eval_(r[1], p)

            cmp, rating, threshold, next_ = r

            if cmps[cmp](p[rating], threshold):
                return eval_(next_, p)

    return sum(sum(part.values()) for part in parts if eval_("in", part))


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
