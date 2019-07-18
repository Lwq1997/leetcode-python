# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 23:02
# @Author  : Lwq
# @File    : maxProfit.py
# @Software: PyCharm
"""
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。
如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，
并将剩余的字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
"""


class Solution:

    @staticmethod
    def reverseString(s, k):
        """
        字符串反转

        使用切片
        :type str: object
        """
        res = ''
        for i in range(0, len(s), 2 * k):
            print(i)
            print(s[i:i + k])
            print(s[i:i + k][::-1])     #前k反转
            print(s[i + k:i + 2 * k])       #后k不反转
            res = res + s[i:i + k][::-1] + s[i + k:i + 2 * k]
        return res


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    res1 = Solution.reverseString(s, k)
    print(res1)
