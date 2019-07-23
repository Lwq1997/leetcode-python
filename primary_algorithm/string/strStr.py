# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     strStr
   Description :
   Author :       lwq
   date：          2019-07-23
-------------------------------------------------
   Change Activity:
                   2019-07-23:
-------------------------------------------------
"""
__author__ = 'lwq'
"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


class Solution:

    @staticmethod
    def strStr(s, k):
        """
        实现strStr()
        :type str: object
        """
        if k not in s:
            return -1
        return s.find(k)

    @staticmethod
    def strStr01(s, k):
        """
        实现strStr()

        使用切片
        :type str: object
        """
        if not k:
            return 0
        l = len(k)
        for i in range(len(s) - l + 1):
            if s[i:l + i] == k:
                return i
        return -1


if __name__ == '__main__':
    s = "abcdefg"
    k = "cd"
    res1 = Solution.strStr(s, k)
    res2 = Solution.strStr01(s, k)
    print(res1)
    print(res2)
