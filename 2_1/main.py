from utils.file_operations import read_lines


CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def main():
    input = read_lines("2_1/input.txt")
    # input = [
    #     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    #     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    #     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    #     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    #     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    # ]
    result = 0
    for index, game in enumerate(input):
        game_record_start = game.find(":") + 1
        game = game[game_record_start:]
        game = game.split(";")
        legal_game = True
        for drawn_set in game:
            cubes: list[str] = drawn_set.split(",")
            for drawn_cubes in cubes:
                drawn_cubes = drawn_cubes.strip()
                drawn_amount, color = drawn_cubes.split(" ")
                drawn_amount = int(drawn_amount)
                if drawn_amount > CUBES[color]:
                    legal_game = False
                    break
            if not legal_game:
                break
        if legal_game:
            result += index + 1
    print(result)


if __name__ == "__main__":
    main()