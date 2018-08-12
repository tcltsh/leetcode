# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addLink(self, head, tail, val):
        now = ListNode(val)
        if head is None:
            head = tail = now
        else:
            tail.next = now
            tail = now
        return head, tail

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = 0
        md = 0
        head = tail = None
        while l1 or l2:
            sum1 = sum2 = 0
            if l1:
                sum1 = l1.val
                l1=l1.next
            if l2:
                sum2 = l2.val
                l2=l2.next
            head, tail = self.addLink(head, tail, (sum1 + sum2 + md) % 10)
            if (sum1 + sum2 + md) >= 10:
                md = 1
            else:
                md = 0
        if md == 1:
            head, tail = self.addLink(head, tail, 1)
        return head

def initClass(datas):
    head = tail = None
    for data in datas:
        now = ListNode(data)
        if head is None:
            head = tail = now
        else:
            tail.next = now
            tail = now
    return head

def initTest():
    return initClass([1]), initClass([9,9])

if __name__ == "__main__":
    a = Solution()
    l1, l2 = initTest()
    ret = a.addTwoNumbers(l1, l2)
    print 'ans:'
    while ret is not None:
        print ret.val
        ret = ret.next
