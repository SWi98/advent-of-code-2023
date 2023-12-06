from utils.file_operations import read_lines
import numpy as np


def main():
    lines = read_lines("4_2/input.txt", rstrip=True)
    # lines = read_lines("4_2/test_input.txt", rstrip=True)
    n = len(lines)
    num_of_cards = [1 for _ in range(n)]
    for i, line in enumerate(lines):
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
            bonus = num_of_cards[i]
            next_card_idx = i + 1
            while next_card_idx < min(matches + i + 1, n):
                num_of_cards[next_card_idx] += bonus
                next_card_idx += 1
    print(sum(num_of_cards))

if __name__ == "__main__":
    main()
