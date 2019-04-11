# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 23:02
# @Author  : Lwq
# @File    : maxProfit.py
# @Software: PyCharm
"""
给定两个数组，编写一个函数来计算它们的交集。（如果交集重复，请完整输出）

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
"""


class Solution:

    @staticmethod
    def intersect(arr1, arr2):
        """
        计算交集

        先算出两个集合中有多少个公共的数字.然后每个数字乘倍数
        :type arr: object
        """
        inter = set(nums1) & set(nums2)
        newarr = []
        for i in inter:
            newarr += [i] * min(nums1.count(i), nums2.count(i))
        return newarr


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1, 3]
    nums2 = [2, 2, 1]
    res1 = Solution.intersect(nums1, nums2)
    print(res1)
