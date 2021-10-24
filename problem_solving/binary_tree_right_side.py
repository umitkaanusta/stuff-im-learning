# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal, take the rightmost at each level
        if root is None:
            return []
        levels = {}
        curr_lvl = 0
        q = deque([root])
        while q:
            n = len(q)
            levels[curr_lvl] = []
            for _ in range(n):
                curr = q.popleft()
                levels[curr_lvl].append(curr.val)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            curr_lvl += 1
        rightmost = []
        for level in levels:
            if levels[level]:
                rightmost.append(levels[level][-1])
        return rightmost
