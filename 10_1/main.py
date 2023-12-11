from utils.file_operations import read_lines
from queue import Queue, LifoQueue
import numpy as np


LEGAL_MOVES = {
    "UP": {
        "S": ["|", "7", "F"],
        "|": ["|", "7", "F", "S"],
        ".": [],
        "-": [],
        "7": [],
        "L": ["|", "7", "F", "S"],
        "F": [],
        "J": ["|", "7", "F", "S"]
    },
    "DOWN": {
        "S": ["|", "L", "J"],
        "|": ["|", "L", "J", "S"],
        ".": [],
        "-": [],
        "7": ["|", "L", "J", "S"],
        "L": [],
        "F": ["|", "L", "J", "S"],
        "J": []
    },
    "LEFT": {
        "S": ["-", "L", "F"],
        "|": [],
        ".": [],
        "-": ["-", "L", "F", "S"],
        "7": ["-", "L", "F", "S"],
        "L": [],
        "F": [],
        "J": ["-", "L", "F", "S"]
    },
    "RIGHT":{
        "S": ["-", "J", "7"],
        "|": [],
        ".": [],
        "-": ["-", "J", "7", "S"],
        "7": [],
        "L": ["-", "J", "7", "S"],
        "F": ["-", "J", "7", "S"],
        "J": []
    },
}


def main() -> int:
    lines = read_lines("10_1/input.txt", rstrip=True)
    # lines = read_lines("10_1/test_input.txt", rstrip=True)
    input: list[list[str]] = []
    for line in lines:
        input.append(["."] + list(line) + ["."])
    row_len = len(input[0])
    column_len = len(input)
    empty_row = ["." for _ in range(row_len)]
    input.append(empty_row)
    input.insert(0, empty_row)
    input = np.array(input)
    print(input)
    nodes = LifoQueue()
    visited = set()
    for i in range(column_len):
        for j in range(row_len):
            if input[i, j] == "S":
                nodes.put(((i, j), 0, (-1, -1)))
                visited.add((i, j))
                break
        if not nodes.empty():
            break
    
    result = None
    while not nodes.empty():
        (col, row), count, (parent_col, parent_row) = nodes.get()
        visited.add((col, row))
        current_node_symbol = input[col, row]
        print(f"CURRENTLY IN {(col, row), current_node_symbol}")
        for idx, direction in [
            ((col-1, row), "UP"),
            ((col+1, row), "DOWN"),
            ((col, row+1), "RIGHT"),
            ((col, row-1), ("LEFT"))
        ]:
            if input[idx] in LEGAL_MOVES[direction][current_node_symbol]:
                if idx not in visited:
                    print(f"ADDING {(idx, count+1), input[idx]}")
                    nodes.put((idx, count + 1, (col, row)))
                elif idx != (parent_col, parent_row) and input[idx] == "S":
                    print("BREAKING")
                    result = col, row, count + 1
                    return result
    print(result)


if __name__ == "__main__":
    res = main()
    print(res)
    print(res[2]/2)
