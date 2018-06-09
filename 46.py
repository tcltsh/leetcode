import copy

class Solution(object):
    def dfs(self, nums, idx):
        if idx == len(nums):
            self.ans.append(copy.deepcopy(nums))
            return
        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            self.dfs(nums, idx+1)
            nums[i], nums[idx] = nums[idx], nums[i]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.dfs(nums, 0)
        return self.ans

if __name__ == "__main__":
    s = Solution()
    print s.permute([1,2,3])
