def solution(seeds, maps):

    def find(val, map_):
        for dest, src, rng in map_:
            if src <= val <= src+rng:
                return dest + (val - src)
        return val

    def traverse(seed):
        soil = find(seed, maps["seed-to-soil"])
        fertilizer = find(soil, maps["soil-to-fertilizer"])
        water = find(fertilizer, maps["fertilizer-to-water"])
        light = find(water, maps["water-to-light"])
        temperature = find(light, maps["light-to-temperature"])
        humidity = find(temperature, maps["temperature-to-humidity"])
        location = find(humidity, maps["humidity-to-location"])
        return location

    return min(map(traverse, seeds))


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
