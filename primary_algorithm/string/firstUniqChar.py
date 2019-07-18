# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 23:02
# @Author  : Lwq
# @File    : maxProfit.py
# @Software: PyCharm
"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.


注意事项：您可以假定该字符串只包含小写字母。
"""
import collections


class Solution:

    @staticmethod
    def firstUniqChar(s):
        """
        字符串中的第一个唯一字符

        使用切片
        :type str: object
        """
        map = {}
        for i in s:
            print(i)
            if i in map:
                map[i] = map[i] + 1
            else:
                map[i] = 0
        for index, i in enumerate(s):
            if map[i] == 0:
                return index
        return -1


    @staticmethod
    def firstUniqChar02(s):
        """
        字符串中的第一个唯一字符

        使用切片
        :type str: object
        """
        dic = collections.Counter(s)
        print(dic)
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    s = "loveleetcode"
    res1 = Solution.firstUniqChar(s)
    res2 = Solution.firstUniqChar02(s)
    print(res1)
    print(res2)
