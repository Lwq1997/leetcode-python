# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 23:02
# @Author  : Lwq
# @File    : maxProfit.py
# @Software: PyCharm
"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false
"""


class Solution:

    @staticmethod
    def containsduplicate(arr):
        """
        判断重复

        使用set
        :type arr: object
        """
        newarr = set(arr)
        if len(newarr) == len(nums):
            return False
        return True


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 7]
    res1 = Solution.containsduplicate(nums)
    print(res1)
