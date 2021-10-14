from collections import deque

"""
Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

EXAMPLE
            5,
    1               2
6       11       3       5

given sum: 12,
num of paths: 3 (5->2->5), (5->1->6) (1->11)
"""


class BTNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left: BTNode = left
        self.right: BTNode = right


def num_paths_with_sum(node: BTNode, sumval: int):
    # Traverse all nodes
    q = deque([node])
    nodes = []
    while q:
        n = len(q)
        for _ in range(n):
            curr = q.popleft()
            nodes.append(curr)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
    # Create hash table sums
    sums = {}
    for node_ptr in nodes[::-1]:
        sums[node_ptr] = []
        sums[node_ptr].append(node_ptr.val)
        if node_ptr.left is not None and sums[node_ptr.left]:
            for val in sums[node_ptr.left]:
                sums[node_ptr].append(node_ptr.val + val)
        if node_ptr.right is not None and sums[node_ptr.right]:
            for val in sums[node_ptr.right]:
                sums[node_ptr].append(node_ptr.val + val)
    # Count sums
    all_sums = []
    for sum_list in sums.values():
        all_sums += sum_list
    return all_sums.count(sumval)


def test_solution():
    tree = BTNode(5, BTNode(1, BTNode(6), BTNode(11)), BTNode(2, BTNode(3), BTNode(5)))
    assert num_paths_with_sum(tree, 12) == 3
    tree2 = BTNode(10, BTNode(5, BTNode(3, BTNode(3), BTNode(-2)),
                              BTNode(1, None, BTNode(2))), BTNode(-3, None, BTNode(11)))
    assert num_paths_with_sum(tree2, 8) == 3


if __name__ == '__main__':
    test_solution()
