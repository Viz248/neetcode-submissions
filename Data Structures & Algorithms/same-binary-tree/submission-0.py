# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        print("\np:",p.val) if p else print("\np:","None")
        print("q:",q.val) if q else print("q:","None")
        if not p and not q:
            return True
        elif (not p and q) or (not q and p):
            return False
        elif p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)