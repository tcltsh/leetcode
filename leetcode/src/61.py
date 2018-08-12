#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 16:05
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 61.py
# @Desc    :

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head is None:
            return None

        total = 0
        cnt = head
        tail = None
        while cnt is not None:
            total += 1
            if cnt is not None and cnt.next == None:
                tail = cnt
            cnt = cnt.next

        if k <= total:
            left_move = total - k
        else:
            md = k % total
            left_move = total - md

        while left_move > 0:
            prehead = head
            tail.next = prehead
            head = head.next
            prehead.next = None
            tail = tail.next
            left_move -= 1

        return head

def make_list():
    vals = [1,2,3,4,5]
    head = None
    tail = None
    for val in vals:
        if head is None:
            head = ListNode(val,None)
            tail = head
        else:
            now = ListNode(val, None)
            tail.next = now
            tail = tail.next
    return head

if __name__ == "__main__":
    s = Solution()
    head = make_list()
    ret = s.rotateRight(head, 8)
    while ret is not None:
        print ret.val
        ret = ret.next

