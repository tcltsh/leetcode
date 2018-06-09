import copy

class Solution(object):
    def dfs(self, left, now_idx, now_ans, nums):
        if left == 0:
            self.ans.append(copy.deepcopy(now_ans))
        if now_idx >= len(nums):
            return
        if nums[now_idx] > left:
            return

        mul = 0
        new_ans = copy.deepcopy(now_ans)
        while mul * nums[now_idx] <= left:
            if mul > 0:
                new_ans.extend([nums[now_idx]])
            self.dfs(left - mul * nums[now_idx], now_idx + 1, new_ans, nums)
            mul += 1


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = []
        candidates.sort()
        self.dfs(target,0, [], candidates)
        return self.ans

if __name__ == "__main__":
    s = Solution()
    print s.combinationSum([2,3,6,7], 7)
