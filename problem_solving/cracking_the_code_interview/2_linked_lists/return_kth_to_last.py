"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""


# ask interviewer: one-indexed or zero-indexed, (assuming one-indexed)


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def kth_to_last(k, node):
    # get length of the list
    list_len = 0
    curr = node
    while curr is not None:
        list_len += 1
        curr = curr.next
    num_jumps = list_len - k
    curr = node
    for _ in range(num_jumps):
        curr = curr.next
    return curr.val


def test_solution():
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 ->
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    assert kth_to_last(1, head) == 6
    assert kth_to_last(2, head) == 5
    assert kth_to_last(3, head) == 4
    assert kth_to_last(4, head) == 3
    assert kth_to_last(5, head) == 2
    assert kth_to_last(6, head) == 1


if __name__ == '__main__':
    test_solution()
