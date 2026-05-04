import sys

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sys.setrecursionlimit(2000)
        curSum = 0 
        def dfs(node):
            nonlocal curSum
            if not node:
                return

            dfs(node.right)
            tmp = node.val
            node.val += curSum 
            curSum += tmp 
            dfs(node.left)
        dfs(root)
        return root