# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        f = head
        s = None
        pre = None
        if f is not None:
            s = f.next

        ret = head

        first_loop = True

        while f is not None and s is not None:
            if first_loop == True:
                ret = s
            first_loop = False

            next = s.next
            f.next = next
            s.next = f
            if pre is not None:
                pre.next = s

            pre = f
            f = next
            s = None
            if f is not None:
                s = f.next

        return ret
