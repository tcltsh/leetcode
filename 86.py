# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        n1 = None
        n2 = None
        pn1 = None
        pn2 = None

        while head is not None:
            next = head.next
            if head.val < x:
                if n1 is None:
                    n1 = head
                    pn1 = n1
                    n1.next = None
                else:
                    n1.next = head
                    n1 = n1.next
                    n1.next = None
            else:
                if n2 is None:
                    n2 = head
                    n2.next = None
                    pn2 = n2
                else:
                    n2.next = head
                    n2 = n2.next
                    n2.next = None
            head = next
        if n1 is not None:
            n1.next = pn2
        if pn1 is None and pn2 is not None:
            return pn2
        return pn1
