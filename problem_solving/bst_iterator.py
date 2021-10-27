# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.idx = 0
        nodes = []
        stack = []
        curr = root
        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                popped = stack.pop()
                nodes.append(popped.val)
                curr = popped.right
            else:
                break
        self.nodes = nodes
        

    def next(self) -> int:
        val = self.nodes[self.idx]
        self.idx += 1
        return val
        
        
    def hasNext(self) -> bool:
        return self.idx != len(self.nodes)
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
