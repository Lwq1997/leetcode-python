# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     deleteNode
   Description :
   Author :       lwq
   date：          2019-07-24
-------------------------------------------------
   Change Activity:
                   2019-07-24:
-------------------------------------------------
"""
__author__ = 'lwq'

"""
删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(head,n):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pre = head
        cur = head
        for i in range(n):
            cur = cur.next

        if cur:
            while cur.next:
                cur = cur.next
                pre = pre.next
            pre.next = pre.next.next
            return head
        else:
            return pre.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    tmp_a = a

    while (tmp_a):
        print(tmp_a.val)
        tmp_a = tmp_a.next

    Solution.removeNthFromEnd(a,2)
    print("+" * 20)

    while (a):
        print(a.val)
        a = a.next
