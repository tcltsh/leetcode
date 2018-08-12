class Solution(object):
    def dfs(self, nums, now, now_ans, ans):
        if now > len(nums):
            return
        ans.append(now_ans[:])
        for i in range(now, len(nums)):
            now_ans.append(nums[i])
            self.dfs(nums, i+1, now_ans, ans)
            now_ans.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(nums, 0, [], ans)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([]))
