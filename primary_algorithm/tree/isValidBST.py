# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     isValidBST
   Description :
   Author :       lwq
   date：          2019-08-02
-------------------------------------------------
   Change Activity:
                   2019-08-02:
-------------------------------------------------
"""
__author__ = 'lwq'

"""
验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        return self.validBST(root, -(2 ** 32), 2 ** 32 - 1)

    def validBST(self, root, small, large):
        if not root:
            return True

        if small >= root.val or large <= root.val:
            return False

        return self.validBST(root.left, small, root.val) and self.validBST(root.right, root.val, large)

    """
    中序遍历后查看链表是不是有序的
    """
    def isValidBST01(self, root: TreeNode) -> bool:
        res = []
        self.search(root, res)
        for i in range(len(res)-1):
            if res[i] >= res[i + 1]:
                return False
        return True

    def search(self, root, res):
        if root:
            self.search(root.left, res)
            res.append(root.val)
            self.search(root.right, res)


if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)

    a.left = b
    a.right = c
    c.left = d
    c.right = e

    print(Solution().isValidBST(a))
    print(Solution().isValidBST01(a))
