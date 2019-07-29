# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     deleteNode
   Description :
   Author :       lwq
   date：          2019-07-29
-------------------------------------------------
   Change Activity:
                   2019-07-29:
-------------------------------------------------
"""
from primary_algorithm.list.ListNode import ListUtility

__author__ = 'lwq'

"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

"""


class Solution:

    def reverseList(self, head):
        if not head or head.next == None:  # 递归终止条件（以及排除特殊值问题）
            return head

        else:
            newhead = self.reverseList(head.next)  # newhead一直是指向最后一个节点
            head.next.next = head
            head.next = None  # 仅仅在第一个元素时候起作用(递归就是一个栈，后进先出，所以先考虑末尾，最后考虑头)
        return newhead

    def reverseList01(self, head):
        pre = head
        cur = head.next
        pre.next = None

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


if __name__ == '__main__':
    utility = ListUtility()
    head = utility.createList(7)
    utility.printList(head)
    # 执行倒转算法，然后再打印队列，前后对比看看倒转是否成功
    reverse = Solution().reverseList(head)
    utility.printList(reverse)
    reverse01 = Solution().reverseList01(reverse)
    utility.printList(reverse01)
