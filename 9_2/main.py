from utils.file_operations import read_lines
from functools import total_ordering
from enum import Enum
import queue
from dataclasses import dataclass
from math import lcm
import numpy as np


def calculate_new_row(row: list[int]) -> list[int]:
    n = len(row)
    new_row = []
    for i in range(1, n):
        new_row.append(row[i] - row[i-1])
    return new_row


def main():
    lines = read_lines("9_2/input.txt", rstrip=True)
    # lines = read_lines("9_2/test_input.txt", rstrip=True)
    data: list[list[int]] = []
    for line in lines:
        data.append([int(x) for x in line.split()])
    result = 0
    for row in data:
        extra_rows = [row]
        while True:
            new_row = calculate_new_row(extra_rows[-1])
            unique_elements = np.unique(new_row)
            if len(unique_elements) == 1 and unique_elements[0] == 0:
                break
            else:
                extra_rows.append(new_row)
        new_element = 0
        for row in extra_rows:
            new_element += row[-1]
        result += new_element
    print(result)


if __name__ == "__main__":
    main()
