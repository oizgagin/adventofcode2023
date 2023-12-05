def solution(seeds, maps):

    def find(vals, map_):
        res = []

        while len(vals) > 0:
            from_, to = vals.pop()

            for dest, src, rng in map_:
                if from_ > src+rng-1:
                    continue
                if to < src:
                    continue
                if src <= from_ and to <= src+rng-1:
                    res.append((dest + (from_ - src), dest + (to - src)))
                    break
                if from_ < src and to <= src+rng-1:
                    vals.append((from_, src-1))
                    res.append((dest, dest + (to - src)))
                    break
                if src <= from_ and src+rng-1 < to:
                    vals.append((src+rng, to))
                    res.append((dest + (from_ - src), dest+rng-1))
                    break

                assert from_ < src and src+rng-1 < to
                vals.append((from_, src-1))
                vals.append((src+rng, to))
                res.append((dest, dest+rng-1))
                break
            else:
                res.append((from_, to))

        return res

    def traverse(seeds):
        soils = find(seeds, maps["seed-to-soil"])
        fertilizers = find(soils, maps["soil-to-fertilizer"])
        waters = find(fertilizers, maps["fertilizer-to-water"])
        lights = find(waters, maps["water-to-light"])
        temperatures = find(lights, maps["light-to-temperature"])
        humidities = find(temperatures, maps["temperature-to-humidity"])
        locations = find(humidities, maps["humidity-to-location"])
        return locations

    res = float("+inf")
    for from_, to in zip(seeds[::2], seeds[1::2]):
        res = min(res, min(map(lambda t: t[0], traverse([(from_, from_+to-1)]))))
    return res


def parse(input):
    seeds, maps = [], {}
    for block in input.split("\n\n"):
        lines = block.splitlines()

        if lines[0].startswith("seeds: "):
            seeds = tuple(map(int, lines[0][len("seeds: "):].split()))
            continue

        name = lines[0].split()[0]
        maps[name] = tuple(map(lambda s: tuple(map(int, s.split())), lines[1:]))

    return seeds, maps


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()