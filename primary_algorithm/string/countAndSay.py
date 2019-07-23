# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     countAndSay
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
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

 

示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"
"""


def countAndSay(n):
    """
    报数
    :type str: object
    """
    basic_num = "1"
    for i in range(n - 1):
        basic_num = transform(basic_num)
    return basic_num


def transform(basic_num):
    num = basic_num[0]
    count = 0
    new_str = ""
    for i in basic_num:
        if num == i:
            count += 1
        else:
            new_str = new_str + str(count) + num
            num = i
            count = 1
    new_str = new_str + str(count) + i
    return new_str


def countAndSay01(n):
    """
    报数
    :type str: object
    """
    if n == 1:
        return "1"

    s = countAndSay01(n - 1)  # !!!!递归

    count = 0  # 某个数字连续出现的次数
    temp_cha = s[0]  # 当前数字
    new_str = ""  # 新的报数序列
    for cha in s:  # 遍历旧的报数序列
        if temp_cha == cha:  # 相同连续数字累加
            count += 1
        else:  # 出现不相同数字就补充新报数序列
            new_str = new_str + str(count) + temp_cha
            temp_cha = cha  # 清零，从头累加新的数字
            count = 1
    new_str = new_str + str(count) + str(temp_cha)  # 最后一个数字补充到新报数序列中

    return new_str


if __name__ == '__main__':
    n = 5
    res = countAndSay(n)
    res1 = countAndSay01(n)
    print(res)
    print(res1)
