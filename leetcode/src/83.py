# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        start = head
        while start.next is not None:
            if start.val == start.next.val:
                start.next = start.next.next
            else:
                start = start.next
        return head

