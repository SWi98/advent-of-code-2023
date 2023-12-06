from utils.file_operations import read_lines
import numpy as np


def main():
    lines = read_lines("4_1/input.txt", rstrip=True)
    # lines = read_lines("4_1/test_input.txt", rstrip=True)
    res = 0
    for line in lines:
        cards = line.split(":")[1]
        winning, mine = cards.split("|")
        mine = mine.strip().split(" ")
        mine = [word for word in mine if word.isnumeric()]
        winning = winning.strip().split(" ")
        winning = [word for word in winning if word.isnumeric()]
        matches = 0
        for my_card in mine:
            if my_card in winning:
                matches += 1
        if matches != 0:
            res += 2 ** (matches - 1)
    print(res)

if __name__ == "__main__":
    main()