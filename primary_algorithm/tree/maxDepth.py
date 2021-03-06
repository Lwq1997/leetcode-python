# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     maxDepth
   Description :
   Author :       lwq
   date：          2019-08-01
-------------------------------------------------
   Change Activity:
                   2019-08-01:
-------------------------------------------------
"""
__author__ = 'lwq'

"""
二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left) + 1
        rightDepth = self.maxDepth(root.right) + 1
        return max(leftDepth, rightDepth)

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.left) + 1
        if root.right is None:
            return self.minDepth(root.right) + 1

        leftDepth = self.minDepth(root.left) + 1
        rightDepth = self.minDepth(root.right) + 1
        return min(leftDepth, rightDepth)


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

    print(Solution().maxDepth(a))
    print(Solution().minDepth(a))
