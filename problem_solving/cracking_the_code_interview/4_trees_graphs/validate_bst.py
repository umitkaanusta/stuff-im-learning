"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""

# idea: if BST, inorder traversal gives a nondecreasing sorted list


class BTNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left: BTNode = left
        self.right: BTNode = right


def is_BST(node: BTNode):
    # Space optimized O(log N) solution using inorder traversal
    stack = []
    """nodes = []"""
    prev_val = None
    curr_val = None
    curr = node
    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        elif stack:
            popped = stack.pop()
            if prev_val is None:
                prev_val = popped.val
            elif curr_val is None:
                curr_val = popped.val
            else:
                prev_val = curr_val
                curr_val = popped.val
            if prev_val is not None and curr_val is not None and prev_val > curr_val:
                return False
            curr = popped.right
        else:
            break
    return True


def test_solution():
    real_BST = BTNode(8, BTNode(4, BTNode(2), BTNode(6)), BTNode(10, None, BTNode(20)))
    not_BST = BTNode(8, BTNode(4, BTNode(2), BTNode(12)), BTNode(10, None, BTNode(20)))
    assert is_BST(real_BST)
    assert not is_BST(not_BST)


if __name__ == '__main__':
    test_solution()
