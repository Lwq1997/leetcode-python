# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 23:02
# @Author  : Lwq
# @File    : maxProfit.py
# @Software: PyCharm
"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""
import collections


class Solution:

    @staticmethod
    def isAnagram(s, t):
        """
        有效的字母异位词

        :type str: object
        """
        dic1 = collections.Counter(s)
        dic2 = collections.Counter(t)
        if dic1.__eq__(dic2):
            return True
        return False

    @staticmethod
    def isAnagram02(s, t):
        return sorted(s) == sorted(t)

    @staticmethod
    def isAnagram03(s, t):
        if len(s) != len(t):
            return False

        c = set(s)
        for i in c:
            if t.count(i) != s.count(i):
                return False
        return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    res1 = Solution.isAnagram(s, t)
    res2 = Solution.isAnagram02(s, t)
    res3 = Solution.isAnagram03(s, t)
    print(res1)
    print(res3)
    print(res2)
