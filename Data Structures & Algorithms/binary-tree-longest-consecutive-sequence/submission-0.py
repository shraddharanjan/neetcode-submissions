# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        self.dfs(root, None, 0)
        return self.max_length

    def dfs(self, p: TreeNode, parent: TreeNode, length: int) -> None:
        if p is None:
            return

        length = length + 1 if parent is not None and p.val == parent.val + 1 else 1
        self.max_length = max(self.max_length, length)

        self.dfs(p.left, p, length)
        self.dfs(p.right, p, length)