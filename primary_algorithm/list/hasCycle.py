# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     deleteNode
   Description :
   Author :       lwq
   date：          2019-07-30
-------------------------------------------------
   Change Activity:
                   2019-07-30:
-------------------------------------------------
"""
from primary_algorithm.list.ListNode import ListUtility, ListNode

__author__ = 'lwq'

"""

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。


 

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

快慢指针相遇点到环入口的距离 = 链表起始点到环入口的距离
"""


class Solution:

    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    utility = ListUtility()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = a
    print(Solution().hasCycle(a))
