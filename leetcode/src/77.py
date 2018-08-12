import copy

class Solution:
    def calc(self,n, total, now, now_flag, now_queue, ans_queue):
        if now == total:
            ans_queue.append(now_queue[:])
            return
        for i in range(now_flag, n + 1):
            if i + total - now_flag > n:
                break
            now_queue.append(i)
            self.calc(n, total, now+1, i + 1, now_queue, ans_queue)
            now_queue.pop(-1)

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        ret = []
        self.calc(n, k, 0, 1, [], ret)
        return ret