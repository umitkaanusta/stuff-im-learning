from collections import deque

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        min_diff = 10000  # range of node values: 0 to 10K
        q = deque([root])
        elements = []
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                elements.append(curr.val)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
        elements.sort(reverse=True)
        for i in range(len(elements) - 1):
            diff = elements[i] - elements[i + 1]
            if diff < min_diff:
                min_diff = diff
        return min_diff
