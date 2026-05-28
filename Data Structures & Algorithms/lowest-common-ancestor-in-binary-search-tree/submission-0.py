# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root
        while True:
            if p.val < root.val and q.val < root.val:
                root = root.left
                res = root
                continue
            elif p.val > root.val and q.val > root.val:
                root = root.right
                res = root
                continue
            break
        return res
            