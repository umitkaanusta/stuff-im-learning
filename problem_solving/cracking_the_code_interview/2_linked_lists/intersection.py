"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.

EXAMPLE
INPUT: 3 -> 1 -> 5 -> 9
                        -> 7 -> 2 -> 1
                 4 -> 6
OUTPUT: 7 -> 2 -> 1

INPUT: 3 -> 1 -> 5 -> 9 -> 7 -> 2 -> 1
       4 -> 6 -> 7 -> 2 -> 1
OUTPUT: False
"""


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def find_intersection(list1, list2):
    # O(n) time, O(1) space
    # make them of same len, find the first node with the same memory id and return it.
    len1 = 0
    len2 = 0
    curr = list1
    while curr is not None:
        len1 += 1
        curr = curr.next
    curr = list2
    while curr is not None:
        len2 += 1
        curr = curr.next
    # make two lists of same length
    if len1 > len2:
        for i in range(len1 - len2):
            list1 = list1.next
    elif len2 > len1:
        for i in range(len2 - len1):
            list2 = list2.next
    # find the intersecting node
    curr1 = list1
    curr2 = list2
    while curr1 is not None and curr2 is not None:
        if id(curr1) == id(curr2):
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next
    return False


def find_intersection_hashtable(list1, list2):
    # O(n) time but smaller T(n), O(n) space
    ht = {}
    curr = list1
    while curr is not None:
        ht[id(curr)] = True
        curr = curr.next
    curr = list2
    while curr is not None:
        if id(curr) in ht:
            return curr
        else:
            ht[id(curr)] = True
        curr = curr.next
    return False


def test_solution():
    intersect = Node(7, Node(2, Node(1)))
    list1_ = Node(3, Node(1, Node(5, Node(9, intersect))))
    list2_ = Node(4, Node(6, intersect))
    assert find_intersection(list1_, list2_)
    assert find_intersection_hashtable(list1_, list2_)
    list3 = Node(3, Node(1, Node(5, Node(9, Node(7, Node(2, Node(1)))))))
    list4 = Node(4, Node(6, Node(7, Node(2, Node(1)))))
    assert not find_intersection(list3, list4)
    assert not find_intersection_hashtable(list3, list4)
    pass


if __name__ == '__main__':
    test_solution()
