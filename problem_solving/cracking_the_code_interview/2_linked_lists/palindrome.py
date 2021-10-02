"""
Palindrome: Implement a function to check if a linked list is a palindrome.

EXAMPLE
INPUT: 1 -> 2 -> 3 -> 2 -> 1
OUTPUT: True

INPUT: 1 -> 2 -> 3 -> 3 -> 2 -> 1
OUTPUT: True

INPUT: 1 -> 2 -> 3 -> 4
OUTPUT: False

"""


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def is_palindrome_stack(node):
    # O(n) time O(n) space
    if node is None or node.next is None:
        # if [] or [2]
        return True
    curr = node
    st = []
    while curr is not None:
        st.append(curr.val)
        curr = curr.next
    curr = node
    while curr is not None:
        if curr.val != st.pop():
            return False
        curr = curr.next
    return True


def reverse_linkedlist_around_pivot(pivot, node):
    # get to the element at pivot
    i = 0
    new = node
    while i != pivot:
        new = new.next
        i += 1
    prev = None
    curr = new
    while curr is not None:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_
    new = prev
    return new


def is_palindrome_nostack(node):
    # O(n) time O(1) space
    # reverse the second half, check if two halves same
    if node is None or node.next is None:
        # if [] or [2]
        return True
    length = 0
    curr = node
    while curr is not None:
        length += 1
        curr = curr.next
    # if length = 9 lets say, mid = 4th idx 1234[5]4321, so we should take mid + 1 as starting pt
    # if length = 8, mid = 4th idx 1234[4]321, so take mid as starting pt
    pivot = length // 2 + 1 if length % 2 == 1 else length // 2
    # reverse the part starting from idx pivot to the end
    new = reverse_linkedlist_around_pivot(pivot, node)
    # check if both halves are equal
    curr = node
    while new is not None:
        if curr.val != new.val:
            return False
        curr = curr.next
        new = new.next
    return True


def test_solution():
    test0 = Node(1, Node(2, Node(3, Node(2, Node(1)))))
    test1 = Node(1, Node(2, Node(3, Node(3, Node(2, Node(1))))))
    test2 = Node(1, Node(2, Node(3, Node(4))))
    assert is_palindrome_stack(test0)
    assert is_palindrome_stack(test1)
    assert not is_palindrome_stack(test2)
    #
    assert is_palindrome_nostack(test0)
    assert is_palindrome_nostack(test1)
    assert not is_palindrome_nostack(test2)


if __name__ == '__main__':
    test_solution()
