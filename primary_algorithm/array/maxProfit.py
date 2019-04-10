# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 23:02
# @Author  : Lwq
# @File    : maxProfit.py
# @Software: PyCharm
"""
假设有一个数组，它的第i个元素是一支给定的股票在第i天的价格。
如果你最多只允许完成一次交易(例如,一次买卖股票),设计一个算法来找出最大利润。


输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。


先计算每两天之间的利润，得到一个n-1的数组，然后计算最大子数组的和
"""


class Solution:

    @staticmethod
    def maxProfit1(arr):
        """
        买卖股票的最佳时机1
        :type arr: object
        """
        minbuy = arr[0]
        maxpro = 0
        for i in range(len(arr)):
            minbuy = min(minbuy, arr[i])
            maxpro = max(maxpro, arr[i] - minbuy)
        return maxpro

    @staticmethod
    def maxProfit2(arr):
        """
        买卖股票的最佳时机1
        :type arr: object
        """
        list = []
        for i in range(len(arr)-1):
            list.append(arr[i+1]-arr[i])
        res = 0
        mid = 0
        for i in range(len(list)):
            if mid+list[i]>0:
                mid+=list[i]
            else:
                mid = 0
            res = max(res,mid)
        return res

if __name__ == '__main__':
    nums = [7, 1, 5, 3, 6, 4]
    res1 = Solution.maxProfit1(nums)
    res2 = Solution.maxProfit2(nums)
    print(res1)
    print(res2)
