# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     isSymmetric
   Description :
   Author :       lwq
   date：          2019-09-17
-------------------------------------------------
   Change Activity:
                   2019-09-17:
-------------------------------------------------
"""
__author__ = 'lwq'

"""
对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class Solution:

    def isSymmetric(self, root: TreeNode):
        if not root:
            return True
        return self.recursiveTree(root.left,root.right)

    def recursiveTree(self, left, right):
        if not left and not right:
            return True
        if not right or not left:
            return False
        if right.val == left.val:
            return self.recursiveTree(left.left,right.right) and self.recursiveTree(left.right, right.left)
        return False

    def isSymmetric01(self, root: TreeNode):
        if not root:
            return True
        nodeList = [root.left,root.right]
        while nodeList:
            lefttmp = nodeList.pop(0)
            righttmp = nodeList.pop(0)
            if not lefttmp and not righttmp:
                continue
            if not lefttmp or not righttmp:
                return False
            if lefttmp.val != righttmp.val:
                return False
            nodeList.append(lefttmp.left)
            nodeList.append(righttmp.right)
            nodeList.append(lefttmp.right)
            nodeList.append(righttmp.left)
        return True

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(4)
    g = TreeNode(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    print(Solution().isSymmetric(a))
    print(Solution().isSymmetric01(a))
