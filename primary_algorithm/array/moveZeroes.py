# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 21:37
# @Author  : Lwq
# @File    : plusOne.py
# @Software: PyCharm
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution:

    @staticmethod
    def moveZeroes(arr):
        """
        移动0

        :type arr: object
        """
        length = len(arr)
        j = 0
        for i in range(length):
            if arr[i] != 0:
                arr[j] = arr[i]
                j += 1
        arr[j:] = (length - j) * [0]
        return arr


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1, 0, 1, 0, 0, 2, 5, 3, 6]
    nums2 = [9, 90, 1, 4, 0, 2, 5, 0, 0, 5, 9]
    res1 = Solution.moveZeroes(nums1)
    res2 = Solution.moveZeroes(nums2)
    print(res1)
    print(res2)
