class TreeNode(left: TreeNode? = null, right: TreeNode? = null) {
    var left: TreeNode = left
    var right: TreeNode = right
}

class Solution {
    fun invertTree(root: TreeNode?): TreeNode? {
        if (root == null) {
            return null
        }
        val left = root.left
        root.left = root.right
        val right = root.right
        root.right = left
        if (root.left != null) {
            invertTree(root.left)
        }
        if (root.right != null) {
            invertTree(root.right)
        }
        return root
    }
}