# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 22:47
# @Author  : Lwq
# @File    : removeduplicates.py
# @Software: PyCharm


"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。
"""


class Solution:

    @staticmethod
    def removeDuplicates(arr):
        """
        删除排序数组中的重复项

        采用两个标记点 number 和 i ，number记录不重复元素的位置，
        i从number的下一个开始遍历数组，如果i位置的数字等于number位置的数字，
        说明该数字重复出现，不予处理；如果i位置的数字不等于number位置的数字，
        说明该数字没有重复，需要放到l的下一位置，并使number加1。
        :type arr: object
        """
        if len(arr) == 0 :
            return 0
        j = 0
        for i in range(len(arr)):
            if arr[j] != arr[i]:
                j += 1
                arr[j] = arr[i]
        return j+1


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7]
    res = Solution.removeDuplicates(nums)
    for i in range(res):
        print(nums[i], end=' ')
