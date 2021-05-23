"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            n = len(q)
            curr_res = []
            for _ in range(n):
                curr = q.popleft()
                if isinstance(curr, Node):
                    curr_res.append(curr.val)
                    if curr.children:
                        q.append(curr.children)
                else:
                    vals = []
                    for c in curr:
                        vals.append(c.val)
                        if c.children:
                            q.append(c.children)
                    curr_res += vals
            res.append(curr_res)
        return res
