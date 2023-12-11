
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


def solve(input: np.ndarray, column_len: int, row_len: int) -> int:
    nodes = LifoQueue()
    visited = set()
    for i in range(column_len):
        for j in range(row_len):
            if input[i, j] == "S":
                nodes.put(((i, j), 0, (-1, -1), [(i, j)]))
                visited.add((i, j))
                break
        if not nodes.empty():
            break
    result = None
    while not nodes.empty():
        (row, col), count, (parent_row, parent_col), traversed_nodes = nodes.get()
        visited.add((row, col))
        current_node_symbol = input[row, col]
        for idx, direction in [
            ((row-1, col), "UP"),
            ((row+1, col), "DOWN"),
            ((row, col+1), "RIGHT"),
            ((row, col-1), ("LEFT"))
        ]:
            if input[idx] in LEGAL_MOVES[direction][current_node_symbol]:
                if idx not in visited:
                    new_traversed_nodes = traversed_nodes + [idx]
                    nodes.put((idx, count + 1, (row, col), new_traversed_nodes))
                elif idx != (parent_row, parent_col) and input[idx] == "S":
                    result = row, col, count + 1, traversed_nodes
                    return result
    print(result)


def main() -> None:
    lines = read_lines("10_2/input.txt", rstrip=True)
    # lines = read_lines("10_2/test_input3.txt", rstrip=True)
    input: list[list[str]] = []
    for line in lines:
        input.append(["."] + list(line) + ["."])
    row_len = len(input[0])
    column_len = len(input)
    empty_row = ["." for _ in range(row_len)]
    input.append(empty_row)
    input.insert(0, empty_row)
    input: np.ndarray = np.array(input)
    result = solve(input, column_len, row_len)
    mask_np = np.ones(input.shape)
    for idx in result[3]:
        mask_np[idx] = 2
    mask = mask_np
    expanded_mask_shape = (mask.shape[0] * 2 - 1, mask.shape[1] * 2 - 1)
    expanded_mask = np.zeros(expanded_mask_shape)
    for i in range(mask_np.shape[0]):
        for j in range(mask_np.shape[1]):
            expanded_mask[i * 2, j * 2] = mask[i, j]
    for i in range(0, expanded_mask.shape[0], 2):
        for j in range(0, expanded_mask.shape[1] - 2, 2):
            og_i = int(i / 2)
            og_j = int(j / 2)
            if (expanded_mask[i, j] == 2 == expanded_mask[i, j + 2]) and (input[og_i, og_j + 1] in LEGAL_MOVES["RIGHT"][input[og_i, og_j]]):
                expanded_mask[i, j + 1] = 2
    
    for j in range(0, expanded_mask.shape[1], 2):
        for i in range(0, expanded_mask.shape[0] - 2, 2):
            og_i = int(i / 2)
            og_j = int(j / 2)
            if (expanded_mask[i, j] == 2 == expanded_mask[i + 2, j]) and (input[og_i + 1, og_j] in LEGAL_MOVES["DOWN"][input[og_i, og_j]]):
                expanded_mask[i + 1, j] = 2

    
    visited = set()
    outside_points = Queue()
    outside_points.put((0, 0))
    while not outside_points.empty():
        current= outside_points.get()
        if current in visited:
            continue
        visited.add(current)
        if expanded_mask[current] in [1, 0]:
            expanded_mask[current] = 3
        row, col = current   
        for new_row, new_col, direction in [
            (row-1, col, "UP"),
            (row+1, col, "DOWN"),
            (row, col+1, "RIGHT"),
            (row, col-1, ("LEFT"))
        ]:
            if not(0 <= new_row < expanded_mask.shape[0] and 0 <= new_col < expanded_mask.shape[1]):
                continue
            if expanded_mask[new_row, new_col] in [1, 0]:
                outside_points.put((new_row, new_col))
    
    res = 0
    for i in range(expanded_mask.shape[0]):
        for j in range(expanded_mask.shape[1]):
            if expanded_mask[i, j] == 1:
                res += 1
    print(res)

if __name__ == "__main__":
    main()
