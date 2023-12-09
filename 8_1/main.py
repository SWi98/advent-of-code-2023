from utils.file_operations import read_lines
from functools import total_ordering
from enum import Enum
import queue
from dataclasses import dataclass


@dataclass
class Node:
    name: int
    left_child: int
    right_child: int

    def __lt__(self, __value: "Node") -> bool:
        return self.name < __value.name
    
    def __eq__(self, __value: "Node") -> bool:
        return self.name == __value.name


def main():
    lines = read_lines("8_1/input.txt", rstrip=True)
    # lines = read_lines("8_1/test_input.txt", rstrip=True)
    instructions = []
    nodes: list[tuple(int, str, str)] = []
    names_mapping = {}
    counter = 0
    for i, line in enumerate(lines):
        if i == 0:
            instructions = list(line.strip())
            continue
        if line.strip() == "":
            continue
        node_name, node_children = line.split("=")
        node_name = node_name.strip()
        names_mapping[node_name] = counter
        node_name = counter
        counter += 1
        node_children = node_children.split()
        left = node_children[0][1:].replace(",", "")
        right = node_children[1][:-1]
        nodes.append((node_name, left, right))
    node_objs: list[Node] = []
    for node in nodes:
        name, left, right = node
        left = names_mapping[left]
        right = names_mapping[right]
        node_objs.append(Node(name=name, left_child=left, right_child=right))
    current_node = node_objs[names_mapping["AAA"]]
    last_node_name = names_mapping["ZZZ"]
    steps = 0
    print(len(node_objs))
    print(current_node.name)
    print(last_node_name)
    print(names_mapping["LNC"])
    node_objs.sort()
    while current_node.name != last_node_name:
        for direction in instructions:
            steps += 1
            if direction == "R":
                current_node = node_objs[current_node.right_child]
            else:
                current_node = node_objs[current_node.left_child]
            if current_node.name == last_node_name:
                break
    print(steps)
if __name__ == "__main__":
    main()
