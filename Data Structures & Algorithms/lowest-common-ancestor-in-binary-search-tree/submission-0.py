# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node=root
        pv, qv = p.val, q.val

        while True:
            n=node.val
            if pv<n and qv<n:
                node=node.left
            elif pv>n and qv>n:
                node=node.right
            else:
                return node