from typing import Optional

from helpers import read_file_as_list

terminal_lines = read_file_as_list("./data/7.txt", str, "")


# 7.a

# Building tree
class Node:
    def __init__(self, name: str, size: int = 0, parent: Optional["Node"] = None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = {}

    @property
    def is_dir(self):
        return bool(self.children)

    def calc_size(self):
        if self.size == 0 and self.is_dir:
            for child in self.children.values():
                child.calc_size()
                self.size += child.size


root_node = Node("/")

curr_node = root_node
for terminal_line in terminal_lines:
    # Navigate to root
    if terminal_line.startswith("$ cd /"):
        curr_node = root_node
        continue

    # Navigate up
    if terminal_line.startswith("$ cd .."):
        curr_node = curr_node.parent
        continue

    # Navigate to sub-folder. Assuming we have listed it before.
    if terminal_line.startswith("$ cd"):
        node_name = terminal_line.split("cd", 1)[1].strip()
        curr_node = curr_node.children[node_name]
        continue

    # If we list, just skip the line
    if terminal_line.startswith("$ ls"):
        continue

    # Parsing responses from list
    size_or_dir, node_name = terminal_line.split()
    size = int(size_or_dir.replace("dir", "0"))

    # if it's a new file or dir add it as a child to the current directory.
    if node_name not in curr_node.children:
        curr_node.children[node_name] = Node(node_name, size, curr_node)

    # Computing size of dirs
root_node.calc_size()


def calc_sum_of_dirs(node: Node, limit: int):
    child_sums = sum(calc_sum_of_dirs(child, limit) for child in node.children.values() if child.is_dir)
    return node.size + child_sums if node.size <= limit else child_sums


print(calc_sum_of_dirs(root_node, 100000))

# 7.b
TOTAL_DISK_SPACE = 70000000
UPDATE_SIZE = 30000000
required_space = UPDATE_SIZE - (TOTAL_DISK_SPACE - root_node.size)


def find_smallest_dir_above_limit(node: Node, limit: int):
    smallest_size = TOTAL_DISK_SPACE

    def _find_smallest_dir_above_limit(node: Node, limit: int):
        if not node.is_dir or node.size < limit:
            return
        nonlocal smallest_size
        if node.size < smallest_size:
            smallest_size = node.size
        for child in node.children.values():
            _find_smallest_dir_above_limit(child, limit)
    _find_smallest_dir_above_limit(node, limit)

    return smallest_size
print(find_smallest_dir_above_limit(root_node, required_space))