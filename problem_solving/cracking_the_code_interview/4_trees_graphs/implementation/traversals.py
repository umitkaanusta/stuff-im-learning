from collections import deque

class BTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_recursive(node: BTNode):
    # Left - Node - Right
    # if done on a binary search tree: the resulting array is ordered ascendingly
    if node is not None:
        inorder_recursive(node.left)
        print(node.val)
        inorder_recursive(node.right)


def inorder_iterative(node: BTNode):
    """
    1) Create an empty stack S.
    2) Initialize current node as root
    3) Push the current node to S and set current = current->left until current is NULL
    4) If current is NULL and stack is not empty then
        a) Pop the top item from stack.
        b) Print the popped item, set current = popped_item->right
        c) Go to step 3.
    5) If current is NULL and stack is empty then we are done.
    """
    nodes = []
    stack = []
    curr = node
    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        elif stack:
            popped = stack.pop()
            nodes.append(popped.val)
            curr = popped.right
        else:
            break
    return nodes


def preorder_recursive(node: BTNode):
    # Node - Left - Right
    # root is always the first node visited
    if node is not None:
        print(node.val)
        preorder_recursive(node.left)
        preorder_recursive(node.right)


def preorder_iterative(node: BTNode):
    """
    1) Create an empty stack nodeStack and push root node to stack.
    2) Do the following while nodeStack is not empty.
        ….a) Pop an item from the stack and print it.
        ….b) Push right child of a popped item to stack
        ….c) Push left child of a popped item to stack
    """
    nodes = []
    stack = [node]
    while stack:
        curr = stack.pop()
        nodes.append(curr.val)
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
    return nodes


def postorder_recursive(node: BTNode):
    # Left - Right - Node
    # root is always the last node visited
    if node is not None:
        postorder_recursive(node.left)
        postorder_recursive(node.right)
        print(node.val)


def postorder_iterative(node: BTNode):
    """
    1. Push root to first stack.
    2. Loop while first stack is not empty
        2.1 Pop a node from first stack and push it to second stack
        2.2 Push left and right children of the popped node to first stack
    3. Reverse second stack, print it
    """
    stack = [node]
    nodes = []
    while stack:
        popped = stack.pop()
        nodes.append(popped.val)
        if popped.left is not None:
            stack.append(popped.left)
        if popped.right is not None:
            stack.append(popped.right)
    return nodes[::-1]


if __name__ == '__main__':
    #            5
    #     4              6
    # 3      4.5    5.5     6.5
    tree = BTNode(val=5,
                  left=BTNode(val=4, left=BTNode(3), right=BTNode(4.5)),
                  right=BTNode(val=6, left=BTNode(5.5), right=BTNode(6.5))
                  )
    print("Inorder:")
    inorder_recursive(tree)
    print(inorder_iterative(tree))

    print("\nPreorder:")
    preorder_recursive(tree)
    print(preorder_iterative(tree))

    print("\nPostorder:")
    postorder_recursive(tree)
    print(postorder_iterative(tree))
