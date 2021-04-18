class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # non-pythonic solution
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    head = ListNode(val=-420)
    curr = head  # pointer to head node
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            curr.next = ListNode(l1.val)
            l1 = l1.next
        else:
            curr.next = ListNode(l2.val)
            l2 = l2.next
        curr = curr.next
    remaining = l2 if l1 is None else l1
    while remaining is not None:
        curr.next = ListNode(remaining.val)
        remaining = remaining.next
        curr = curr.next
    return head.next


l_124 = ListNode(1)
l_124.next = ListNode(2)
l_124.next.next = ListNode(4)

l_134 = ListNode(1)
l_134.next = ListNode(3)
l_134.next.next = ListNode(4)

l_m93 = ListNode(-9, next_=ListNode(3))
l_57 = ListNode(5, next_=ListNode(7))


def ll_to_str(li: ListNode):
    if li is None:
        return None
    string = ""
    while li is not None:
        string += str(li.val) + " "
        li = li.next
    return string[:-1]  # remove the ending space


if __name__ == '__main__':
    assert ll_to_str(mergeTwoLists(l_m93, l_57)) == "-9 3 5 7"
    assert ll_to_str(mergeTwoLists(l_124, l_134)) == "1 1 2 3 4 4"
    assert ll_to_str(mergeTwoLists(None, None)) is None
    assert ll_to_str(mergeTwoLists(None, ListNode())) == "0"
