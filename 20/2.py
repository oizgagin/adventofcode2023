import collections
import fractions


def solution(modules):
    c = collections.defaultdict(list)
    for s, (_, ds) in modules.iteritems():
        for d in ds:
            if d in set(k for k, v in modules.iteritems() if v[0] == "&"): c[d].append(s)

    def inc(sig):
        attr = "his" if sig == "high" else "los"
        setattr(inc, attr, getattr(inc, attr, 0) + 1)

    def inv(sig):
        return "low" if sig == "high" else "high"

    def type_(mod):
        return modules[mod][0] if mod in modules else None

    def next_(mod):
        return modules[mod][1] if mod in modules else []

    def switch(mod):
        switch.states = getattr(switch, "states", {})
        if switch.states.get(mod, False) == False:
            switch.states[mod] = True
            return "high"
        switch.states[mod] = False
        return "low"

    records = {}

    def conj(mod, src, sig, i):
        conj.inputs = getattr(conj, "inputs", {})
        if mod not in conj.inputs:
            conj.inputs[mod] = {}
            for n in c[mod]: conj.inputs[mod][n] = "low"

        conj.inputs[mod][src] = sig

        if all(v == "high" for v in conj.inputs[mod].values()):
            return "low"

        if mod not in records:
            records[mod] = (i, False)
        else:
            records[mod] = (i - records[mod][0], True)

        return "high"

    def eval_(s, i):
        inc("low")

        q = [s]

        while len(q) > 0:
            mod, src, sig = q.pop(0)

            if type_(mod) == "%":
                if sig == "low":
                    next_sig = switch(mod)
                    for n in next_(mod):
                        inc(next_sig)
                        q.append((n, mod, next_sig))

            elif type_(mod) == "&":
                next_sig = conj(mod, src, sig, i)
                for n in next_(mod):
                    inc(next_sig)
                    q.append((n, mod, next_sig))

            else:
                for n in next_(mod):
                    inc(sig)
                    q.append((n, mod, sig))

    inrx = [mod for mod in modules.keys() if "rx" in modules[mod][1]]
    assert len(inrx) == 1
    inrx = inrx[0]

    assert inrx in c
    mods = c[inrx]

    i = 0
    while True:
        i += 1
        eval_(("broadcaster", "", "low"), i)

        if all((mod in records and records[mod][1]) for mod in mods):
            return reduce(
                lambda x, y: (x * y) / fractions.gcd(x, y),
                [records[mod][0] for mod in mods],
                records[mods[0]][0]
            )


def parse(input):
    res = dict()
    for line in input.splitlines():
        src, dests = tuple(line.split(" -> "))
        dests = dests.split(", ")
        if src[0] in "%&":
            res[src[1:]] = (src[0], dests)
        else:
            res[src] = (None, dests)
    return res


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
