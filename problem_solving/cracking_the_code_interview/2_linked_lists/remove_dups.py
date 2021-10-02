"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

# additional question: should i keep the first occurence of two duplicates?


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def remove_duplicates_buffer(node: Node):
    # O(n) time, O(n) space
    ht = {}  # we could've used a bit vector if we knew the bounds of the numbers
    prev = None
    while node is not None:
        if node.val not in ht:
            ht[node.val] = True
            prev = node
        else:
            prev.next = node.next
        node = node.next


def remove_duplicates_nobuffer(node: Node):
    # O(n^2) time, O(1) space
    curr = node
    while curr is not None:
        i = curr
        while i.next is not None:
            if curr.val == i.next.val:
                i.next = i.next.next
            else:
                i = i.next
        curr = curr.next


def test_solution():
    # 3 -> 2 -> 4 -> 3 -> 5 -> 5 -> 3 ->
    # 3 -> 2 -> 4 -> 5 ->
    head = Node(val=3)
    head.next = Node(val=2)
    head.next.next = Node(val=4)
    head.next.next.next = Node(val=3)
    head.next.next.next.next = Node(val=5)
    head.next.next.next.next.next = Node(val=5)
    head.next.next.next.next.next.next = Node(val=3)
    remove_duplicates_nobuffer(head)
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next

    print()
    head = Node(val=3)
    head.next = Node(val=2)
    head.next.next = Node(val=4)
    head.next.next.next = Node(val=3)
    head.next.next.next.next = Node(val=5)
    head.next.next.next.next.next = Node(val=5)
    head.next.next.next.next.next.next = Node(val=3)
    remove_duplicates_buffer(head)
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


if __name__ == '__main__':
    test_solution()
