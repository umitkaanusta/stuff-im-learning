# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque([root])
        depth = 0
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            depth += 1
        return depth
      
