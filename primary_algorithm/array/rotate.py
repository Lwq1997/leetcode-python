# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 23:02
# @Author  : Lwq
# @File    : maxProfit.py
# @Software: PyCharm
"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
"""


class Solution:

    @staticmethod
    def rotate(arr, k):
        """
        旋转数组

        使用切片
        :type arr: object
        """
        newk = k % len(arr)
        print(arr[-newk:])
        print(arr[:-newk])
        arr[:] = arr[-newk:] + arr[:-newk]
        return arr

    @staticmethod
    def rotate2(arr, k):
        """
        旋转数组

        使用循环，每次移动一位
        :type arr: object
        """
        l = len(arr)
        k %= l
        if not k:
            for i in range(k):
                temp = arr[l - 1]
                j = l - 1
                while j > 0:
                    arr[j] = arr[j - 1]
                    j -= 1
                arr[0] = temp
        return arr


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    res1 = Solution.rotate(nums, k)
    res2 = Solution.rotate2(nums, k)
    print(res1)
    print(res2)
