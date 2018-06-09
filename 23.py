# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Heap:
    def __init__(self):
        self.val = []
        self.total = 0

    def push(self, newval):
        self.val.append(newval)
        self.total += 1
        self.resort()

    def pop(self):
        self.val[0], self.val[self.total - 1] = self.val[self.total - 1], self.val[0]
        ret = self.val.pop()
        self.total -= 1
        self.resortPop()
        return ret

    def resort(self):
        now = self.total
        while now > 1:
            parent = now // 2
            if self.val[parent - 1].val > self.val[now - 1].val:
                self.val[now - 1], self.val[parent - 1] = self.val[parent - 1], self.val[now - 1]
                now = parent
            else:
                break

    def resortPop(self):
        now = 0
        while now < self.total:
            left = (now + 1) * 2 - 1
            right = (now + 1) * 2

            swap_idx = now
            swap_value = self.val[now].val

            if left < self.total and self.val[left].val < swap_value:
                swap_value = self.val[left].val
                swap_idx = left

            if right < self.total and self.val[right].val < swap_value:
                swap_value = self.val[right].val
                swap_idx = right

            if swap_idx == now:
                break

            self.val[now], self.val[swap_idx] = self.val[swap_idx], self.val[now]
            now = swap_idx


    def size(self):
        return self.total

    def printHeap(self):
        print '---------begin'
        for i in range(0, self.total):
            print self.val[i].val
        print '---------over'

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        hp = Heap()
        for node in lists:
            if node is not None:
                hp.push(node)
        ret = None
        next = None

        while hp.size() > 0:
            now = hp.pop()
            if now.next is not None:
                hp.push(now.next)
            newNode = ListNode(now.val)
            if ret is None:
                ret = newNode
                next = ret
            else:
                next.next = newNode
                next = next.next
        return ret
