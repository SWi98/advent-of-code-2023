from utils.file_operations import read_lines
import numpy as np


def main():
    lines = read_lines("3_2/input.txt", rstrip=True)
    input = []
    for line in lines:
        input.append(["."] + list(line) + ["."])
    empty_row = ["." for _ in range(len(input[0]))]
    input.append(empty_row)
    input.insert(0, empty_row)

    width, height = len(input[0]), len(input)
    res = 0
    for h in range(1, height):
        for w in range(1, width):
            found_numbers = []
            found_indexes = set()
            if input[h][w] == "*":
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        new_h = h + i
                        new_w = w + j
                        number = ""
                        while new_w < width and input[new_h][new_w].isnumeric():
                            number += input[new_h][new_w]
                            new_w += 1
                        new_w = w + j
                        first_skipped = False
                        while new_w > 0 and input[new_h][new_w].isnumeric():
                            if not first_skipped:
                                # skip adding the first sign since it was added in the previous loop
                                first_skipped = True
                            else:
                                number = input[new_h][new_w] + number
                            new_w -= 1
                        if number != "":
                            if (new_h, new_w) not in found_indexes:
                                found_indexes.add((new_h, new_w))
                                found_numbers.append(int(number))
            if len(found_numbers) == 2:
                res += found_numbers[0] * found_numbers[1]

    print(res)

if __name__ == "__main__":
    main()