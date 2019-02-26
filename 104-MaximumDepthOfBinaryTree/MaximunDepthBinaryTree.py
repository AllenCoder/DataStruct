# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lefeHight = self.maxDepth(root.left) + 1
        rightHight = self.maxDepth(root.right) + 1

        return max(lefeHight, rightHight)
