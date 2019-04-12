# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 21:37
# @Author  : Lwq
# @File    : plusOne.py
# @Software: PyCharm
"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""


class Solution:

    @staticmethod
    def plusOne(arr):
        """
        加一

        :type arr: object
        """
        length = len(arr)
        for i in range(length - 1, -1, -1):
            if arr[i] < 9:
                arr[i] += 1
                return arr
            arr[i] = 0
        return [1] + arr


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [9, 9]
    res1 = Solution.plusOne(nums1)
    res2 = Solution.plusOne(nums2)
    print(res1)
    print(res2)
