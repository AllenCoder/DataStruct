# 反转二叉树

输入：
```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
 
 
```
输出
 
 
```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

-【思路一】:采用递归思路先invertTree(root.left and root.right)，然后再交换root.left和root.right
-【思路二】：采用Stack栈模拟压入和弹出，改变顺序