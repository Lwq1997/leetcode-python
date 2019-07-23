# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     longestCommonPrefix
   Description :
   Author :       lwq
   date：          2019-07-23
-------------------------------------------------
   Change Activity:
                   2019-07-23:
-------------------------------------------------
"""
from typing import List

__author__ = 'lwq'
"""
最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""


class Solution:
    def longestCommonPrefix(strs) -> str:
        res = ""
        if len(strs) == 0:
            return ""

        for each in zip(*strs):
            print(each)
            if len(set(each)) == 1:  # 利用集合创建一个无序不重复元素集
                res += each[0]
            else:
                return res
        return res

    def longestCommonPrefix01(strs) -> str:
        if len(strs) == 0:
            return ""

        a = min(strs)
        b = max(strs)

        for i in range(len(a)):
            if a[i] != b[i]:
                return a[:i]
        return a


if __name__ == '__main__':
    list = ["flower", "flow", "flight"]
    print(Solution.longestCommonPrefix(list))
    print(Solution.longestCommonPrefix01(list))
