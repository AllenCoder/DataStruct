# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inOrder = self.inOrder(root)
        return inOrder == list(sorted(set(inOrder)))

    def inOrder(self, root):
        if root is None:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
