# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self, t: Optional[TreeNode]) -> bool:
        return t.left is None and t.right is None

    def addLeaves(self, res: List[int], root: Optional[TreeNode]) -> None:
        if self.isLeaf(root):
            res.append(root.val)
        else:
            if root.left is not None:
                self.addLeaves(res, root.left)
            if root.right is not None:
                self.addLeaves(res, root.right)

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res

        if not self.isLeaf(root):
            res.append(root.val)

        t = root.left
        while t is not None:
            if not self.isLeaf(t):
                res.append(t.val)
            if t.left is not None:
                t = t.left
            else:
                t = t.right

        self.addLeaves(res, root)

        stack = []
        t = root.right
        while t is not None:
            if not self.isLeaf(t):
                stack.append(t.val)
            if t.right is not None:
                t = t.right
            else:
                t = t.left

        while stack:
            res.append(stack.pop())

        return res