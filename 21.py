# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addLink(self, head, tail, node):
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = tail.next
        node = node.next
        return head, tail, node

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tail = None
        while l1 or l2:
            if l2 is None and l1 is not None:
                head, tail, l1 = self.addLink(head, tail, l1)
                continue
            if l1 is None and l2 is not None:
                head, tail, l2 = self.addLink(head, tail, l2)
                continue
            if l1.val < l2.val:
                head, tail, l1 = self.addLink(head, tail, l1)
                continue
            if l2.val <= l1.val:
                head, tail, l2 = self.addLink(head, tail, l2)
                continue
        if tail:
            tail.next = None
        return head
