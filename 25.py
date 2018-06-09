# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, begin, pre, tail, k):
        nhead = None
        ntail = None
        if k == 2:
            end = begin.next
            end.next = begin
            nhead = end
            ntail = begin
        else:
            ntail = begin
            a = begin
            b = a.next

            while b != tail:
                nhead = b
                next = b.next
                b.next = a

                a = b
                b = next

        if pre is not None:
            pre.next = nhead
        ntail.next = tail
        return nhead, ntail



    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k < 2:
            return head

        pre = None
        ret = head
        tail = head
        begin = head
        count = 0

        while tail is not None:
            count += 1
            if count == k:
                count = 0
                next = tail.next
                nhead, ntail = self.reverse(begin, pre, next, k)
                if pre is None:
                    ret = nhead
                pre = ntail
                begin  = tail = next
            else:
                tail = tail.next
        return ret
