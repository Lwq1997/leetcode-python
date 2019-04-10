# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 23:15
# @Author  : Lwq
# @File    : maxProfit2.py
# @Software: PyCharm
"""

假设有一个数组，它的第i个元素是一支给定的股票在第i天的价格。
交易次数不限，但一次只能交易一支股票，也就是说手上最多只能持有一支股票，求最大收益。


输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。


当明天的价格比今天的价格贵的时候我们今天买，明天卖，这样能够获取最大利润。

"""


class Solution:

    @staticmethod
    def maxProfit(arr):
        """
        买卖股票的最佳时机2
        :type arr: object
        """
        profit = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                profit += arr[i] - arr[i - 1]
        return profit


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    res = Solution.maxProfit(nums)
    print(res)
