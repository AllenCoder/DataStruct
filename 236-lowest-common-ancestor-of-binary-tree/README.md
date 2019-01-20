# 解题思路

1. 遍历整个树
2. 查找左子树 left
3. 查找右子树 right
4. 当 p <root < q 时 说明root 就是他们的根结点
5. 当前的结点就是他们的公共祖先

二叉树 遍历代码
> 前序遍历

```Python
class TreeNode(object):
    def __init__(self):
        self.traverse_path = []
        self.left = None
        self.right = None
        self.val = None

    def preorder(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            self.traverse_path.append(root.val)
```