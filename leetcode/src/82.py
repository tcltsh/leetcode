# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import copy

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        start = ListNode(0)
        start.val = None
        start.next = head
        head = start

        while start.next is not None:
            now_begin = start.next
            now_loop = now_begin.next
            has = False
            while now_loop is not None:
                if now_loop.val == now_begin.val:
                    has = True
                    now_loop = now_loop.next
                else:
                    break

            if has:
                start.next = now_loop
            else:
                start = start.next
        return head.next

