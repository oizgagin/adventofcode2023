import collections


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

    def conj(mod, src, sig):
        conj.inputs = getattr(conj, "inputs", {})
        if mod not in conj.inputs:
            conj.inputs[mod] = {}
            for n in c[mod]: conj.inputs[mod][n] = "low"

        conj.inputs[mod][src] = sig

        if all(v == "high" for v in conj.inputs[mod].values()):
            return "low"

        return "high"

    def eval_(s):
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
                next_sig = conj(mod, src, sig)
                for n in next_(mod):
                    inc(next_sig)
                    q.append((n, mod, next_sig))

            else:
                for n in next_(mod):
                    inc(sig)
                    q.append((n, mod, sig))

    for _ in xrange(0, 1000):
        eval_(("broadcaster", "", "low"))

    return inc.his * inc.los


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
