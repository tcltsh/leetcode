# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        ret = head
        pre_node = head
        tail = head
        for i in range(0, n):
            tail = tail.next

        if tail is None:
            ret = ret.next
            return ret

        while tail.next != None:
            tail = tail.next
            pre_node = pre_node.next
        del_node = pre_node.next
        pre_node.next = del_node.next
        del_node.next = None
        return head

