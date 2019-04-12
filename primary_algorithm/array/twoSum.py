# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 21:37
# @Author  : Lwq
# @File    : plusOne.py
# @Software: PyCharm
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:

    @staticmethod
    def twoSum(arr, target):
        """
        两数之和

        使用字典结构
        :type arr: object
        """
        hashmap = {}
        for index, num in enumerate(arr):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index


if __name__ == '__main__':
    nums1 = [2, 2, 11, 15]
    target = 4
    res1 = Solution.twoSum(nums1, target)
    print(res1)
