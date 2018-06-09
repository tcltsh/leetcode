import copy

class Solution(object):
    def dfs(self, left, now_idx, now_ans, nums, cntnums):
        if left == 0:
            self.ans.append(copy.deepcopy(now_ans))
        if now_idx >= len(nums):
            return
        if nums[now_idx] > left:
            return

        mul = 0
        new_ans = copy.deepcopy(now_ans)
        while mul * nums[now_idx] <= left and mul <= cntnums[now_idx]:
            if mul > 0:
                new_ans.extend([nums[now_idx]])
            self.dfs(left - mul * nums[now_idx], now_idx + 1, new_ans, nums, cntnums)
            mul += 1


    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []
        self.ans = []
        candidates.sort()
        input = []
        cnt = []

        last_cnt = 1
        last_num = candidates[0]
        for i in range(1, len(candidates)):
            if candidates[i] == candidates[i-1]:
                last_cnt += 1
            else:
                input.append(last_num)
                cnt.append(last_cnt)
                last_cnt = 1
                last_num = candidates[i]
        input.append(last_num)
        cnt.append(last_cnt)

        self.dfs(target,0, [], input, cnt)
        return self.ans

if __name__ == "__main__":
    s = Solution()
    print s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)