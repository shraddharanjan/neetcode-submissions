# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # for each node in the tree, we will maintain three values
    class State:
        def __init__(self, nodes, sum_val, max_average):
            # count of nodes in the subtree
            self.node_count = nodes
            # sum of values in the subtree
            self.value_sum = sum_val
            # max average found in the subtree
            self.max_average = max_average

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        return self.max_average(root).max_average

    def max_average(self, root):
        if root is None:
            return self.State(0, 0, 0)

        # postorder traversal, solve for both child nodes first.
        left = self.max_average(root.left)
        right = self.max_average(root.right)

        # now find nodeCount, valueSum and maxAverage for current node `root`
        node_count = left.node_count + right.node_count + 1
        sum_val = left.value_sum + right.value_sum + root.val
        max_average = max(
            (1.0 * sum_val) / node_count,  # average for current node
            max(right.max_average, left.max_average)  # max average from child nodes
        )

        return self.State(node_count, sum_val, max_average)