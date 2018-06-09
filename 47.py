import copy

class Solution(object):
    def dfs(self, nums, nowans, idx, totallen):
        if idx == totallen:
            self.ans.append(copy.deepcopy(nowans))
            return
        for k, v in nums.items():
            if v > 0:
                nums[k] -= 1
                self.dfs(nums, nowans + [k], idx +1, totallen)
                nums[k] += 1

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cntnum = {}
        for num in nums:
            if cntnum.has_key(num) is False:
                cntnum[num] = 0
            cntnum[num] += 1
        self.ans = []
        self.dfs(cntnum,[], 0, len(nums))
        return self.ans

if __name__ == "__main__":
    s = Solution()
    print s.permuteUnique([1,1,3])