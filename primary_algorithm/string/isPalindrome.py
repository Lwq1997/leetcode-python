# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 23:02
# @Author  : Lwq
# @File    : maxProfit.py
# @Software: PyCharm
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""


class Solution:

    @staticmethod
    def isPalindrome(s):
        """
        验证回文字符串

        :type str: object
        """
        s1 = []
        for i in s:
            if i.isalnum():
                s1.append(i.lower())
        return True if s1 == s1[::-1] else False


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    res1 = Solution.isPalindrome(s)
    print(res1)
