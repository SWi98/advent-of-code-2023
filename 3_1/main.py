from utils.file_operations import read_lines
import numpy as np


def is_symbol(char: str) -> bool:
    return char != "." and not char.isnumeric()


def main():
    lines = read_lines("3_1/input.txt", rstrip=True)
    input = []
    for line in lines:
        input.append(list(line))

    width, height = len(input[0]), len(input)
    mask = np.zeros((height + 1, width + 1))
    for h in range(1, height + 1):
        for w in range(1, width + 1):
            if is_symbol(input[h-1][w-1]):
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        mask[h+i][w+j] = 1
                        
    res = 0
    for h in range(height):
        w = -1
        while w < width:
            w += 1
            legit_number = False
            number = ""
            while w < width and input[h][w].isnumeric():
                number += input[h][w]
                if mask[h+1][w+1] and not legit_number:
                    legit_number = True
                w += 1
            if legit_number:
                res += int(number)
    print(res)

if __name__ == "__main__":
    main()