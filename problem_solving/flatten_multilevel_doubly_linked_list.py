"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        new = Node(head.val)
        new_ptr = new
        stack = []
        curr = head
        while True:
            if curr is not None:
                if curr.val != head.val:
                    new_ptr.next = Node(curr.val)
                    new_ptr.next.prev = new_ptr
                    new_ptr = new_ptr.next
                if curr.child is not None:
                    stack.append(curr.next)
                    curr = curr.child
                else:
                    curr = curr.next
            elif stack:
                curr = stack.pop()
            else:
                break
        return new
        
        
