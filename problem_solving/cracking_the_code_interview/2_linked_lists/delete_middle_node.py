"""
Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.

EXAMPLE

Input: the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
"""


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def remove_middle_node(remove_val, node):
    curr = node
    while curr.next is not None:
        if curr.next.val == remove_val:
            curr.next = curr.next.next
        curr = curr.next


def test_solution():
    head = Node("a", Node("b", Node("c", Node("d", Node("e", Node("f"))))))
    remove_middle_node("c", head)
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


if __name__ == '__main__':
    test_solution()
