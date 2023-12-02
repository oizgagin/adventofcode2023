import re

def solution(games):

    max_ = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    return sum(
        game[0] for game in games if all(
            all(set_.get(color, 0) <= max_[color] for color in max_.keys())
            for set_ in game[1]
        )
    )


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
