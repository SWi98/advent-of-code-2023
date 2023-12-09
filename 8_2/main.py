from utils.file_operations import read_lines
from functools import total_ordering
from enum import Enum
import queue
from dataclasses import dataclass
from math import lcm


@dataclass
class Node:
    name: int
    left_child: int
    right_child: int

    def __lt__(self, __value: "Node") -> bool:
        return self.name < __value.name
    
    def __eq__(self, __value: "Node") -> bool:
        return self.name == __value.name


def solve(current_node: Node, node_objs: list[Node], instructions: list[str], names_mapping_itos: dict):
    steps = 0
    while True:
        for direction in instructions:
            if direction == "R":
                current_node = node_objs[current_node.right_child]
            elif direction == "L":
                current_node = node_objs[current_node.left_child]
            steps += 1
            if names_mapping_itos[current_node.name][-1] == "Z":
                return steps
    

def main() -> int:
    lines = read_lines("8_2/input.txt", rstrip=True)
    # lines = read_lines("8_2/test_input.txt", rstrip=True)
    instructions = []
    nodes: list[tuple(int, str, str)] = []
    names_mapping = {}
    names_mapping_itos = {}
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
        names_mapping_itos[counter] = node_name
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
    node_objs.sort()
    current_nodes: list[Node] = []
    for str_name, int_name in names_mapping.items():
        if str_name[-1] == "A":
            current_nodes.append(node_objs[int_name])
    counts = []
    for node in current_nodes:
        counts.append(solve(node, node_objs, instructions, names_mapping_itos))
    print(counts)
    print(lcm(*counts))

            

if __name__ == "__main__":
    print(main())
