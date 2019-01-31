class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        lhead = head
        for i in range(0, m - 2):
            lhead = lhead.next

        record_head = lhead
        pre_head = None

        if m > 1:
            lhead = lhead.next
        if lhead == head:
            record_head = None

        subhead = lhead
        head1 = None

        while m <= n:
            head1 = lhead.next
            lhead.next = pre_head
            pre_head = lhead
            lhead = head1

            m += 1

        subhead.next = head1
        if record_head is not None:
            record_head.next = pre_head
            return head
        else:
            return pre_head

