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
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


class Solution:

    def isPalindrome(self, head):
        nodeList = []
        while head:
            nodeList.append(head.val)
            head = head.next
        for i in range(len(nodeList) // 2):
            if nodeList[i] != nodeList[len(nodeList) - i - 1]:
                return False
        return True

    def isPalindrome01(self, head):
        if head is None:
            return True
        if head.next is None:
            return True

        slow = fast = head

        # 1. 定中点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 快慢指针定位中点，此时fast已到达链尾，如果长度为奇数，则slow到达中心点，长度为偶数，则slow到达下中位点

        # 2. 后半段倒置
        pre = None  # 倒置后的最后一个节点必为None,以此确定第三步遍历时的终点
        cur = slow  # 当前要倒置的第一个节点
        nxt = slow.next  # 当前要倒置的节点的下一个节点

        while nxt:  # 只要没有到达原链表的终点就一直进行倒置
            cur.next = pre  # 将当前节点的下一个节点指向"前"一个节点，进行倒置

            # 相邻节点倒置完成后，向后整体偏移1个单位
            pre = cur
            cur = nxt
            nxt = cur.next
        # 当前cur是最后一个节点，需要和它前面的节点进行最后一次倒置，来完成整个后半段倒置

        cur.next = pre

        # 3. cur就是倒置完成后的后半段的头节点,同时遍历cur和head，如果遍历完cur未出现不同的节点，则为回文链表

        while cur.next:
            if cur.val != head.val:
                return False
            cur = cur.next
            head = head.next
        # 此时cur为后半段的最后一个节点，还需要判断此时的cur和head的值是否相同

        return cur.val == head.val


if __name__ == '__main__':
    utility = ListUtility()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    Solution().isPalindrome01(a)
    utility.printList(a)
