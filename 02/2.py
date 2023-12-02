import re

def solution(games):
    product = lambda it: reduce(lambda acc, x: acc * x, it, 1)

    return sum(map(
        lambda game: product(
            (max(set_.get(color, 0) for set_ in game[1]))
            for color in ["red", "blue", "green"]
        ),
        games
    ))


def parse(input):

    def parse_game(line):
        id_ = int(line.split(":")[0][len("Game "):])

        sets = []
        for set_ in line.split(":")[1].split(";"):
            s = {}
            for cube in set_.split(","):
                s[cube.split()[1]] = int(cube.split()[0])
            sets.append(s)

        return (id_, sets)

    return map(parse_game, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
