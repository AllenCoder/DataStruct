
# 解题思路

1. 对二叉树进行中序遍历，将遍历后的结果存放到数组inorder里面
2. 将原二叉树进行去重放入Set集合 set
3. 将se集合排序 list
4. 判断 list == inoreder 即为有效的二叉树