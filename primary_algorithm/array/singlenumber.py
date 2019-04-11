# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 23:02
# @Author  : Lwq
# @File    : maxProfit.py
# @Software: PyCharm
"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
"""


class Solution:

    @staticmethod
    def singlenumber(arr):
        """
        只出现一次的数字

        一个数异或自身是0,0异或任何数都是那个数
        :type arr: object
        """
        num = 0
        for i in range(len(arr)):
            num ^= arr[i]
        return num


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 3, 5, 5]
    res1 = Solution.singlenumber(nums)
    print(res1)
