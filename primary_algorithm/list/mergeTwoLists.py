# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mergeTwoLists
   Description :
   Author :       lwq
   date：          2019-07-29
-------------------------------------------------
   Change Activity:
                   2019-07-29:
-------------------------------------------------
"""
__author__ = 'lwq'

"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            ret = l1
            ret.next = self.mergeTwoLists(l1.next, l2)
        else:
            ret = l2
            ret.next = self.mergeTwoLists(l1, l2.next)
        return ret


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    head1 = ListNode(2)
    n1 = ListNode(3)
    n2 = ListNode(4)
    n3 = ListNode(9)
    head1.next = n1
    n1.next = n2
    n2.next = n3

    head2 = ListNode(3)
    m1 = ListNode(5)
    m2 = ListNode(7)
    m3 = ListNode(8)
    head2.next = m1
    m1.next = m2
    m2.next = m3

    res = Solution().mergeTwoLists(head1, head2);

    while res:
        print(res.val)
        res = res.next
