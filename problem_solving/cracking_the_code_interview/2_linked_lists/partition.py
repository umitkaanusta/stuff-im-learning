"""
Partition:
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def partition_list(partition_val, node):
    smaller = None
    gt_equal = None
    curr = node
    curr_small = smaller
    curr_gt_equal = gt_equal
    while curr is not None:
        if curr.val < partition_val:
            if smaller is None:
                smaller = Node(curr.val)
                curr_small = smaller
            else:
                curr_small.next = Node(curr.val)
                curr_small = curr_small.next
        else:
            if gt_equal is None:
                gt_equal = Node(curr.val)
                curr_gt_equal = gt_equal
            else:
                curr_gt_equal.next = Node(curr.val)
                curr_gt_equal = curr_gt_equal.next
        curr = curr.next
    curr_small.next = gt_equal
    return smaller


def test_solution():
    head = Node(3, Node(5, Node(8, Node(5, Node(10, Node(2, Node(1)))))))
    head = partition_list(5, head)
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


if __name__ == '__main__':
    test_solution()
