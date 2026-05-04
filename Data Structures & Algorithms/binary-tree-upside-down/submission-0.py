# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr, prev, prev_right = root, None, None

        while curr:
            next_node = curr.left
            right = curr.right

            curr.left = prev_right
            curr.right = prev

            prev = curr
            prev_right = right
            curr = next_node

        return prev
