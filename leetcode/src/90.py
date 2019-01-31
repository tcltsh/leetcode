class Solution:
    def dfs(self, index, nums, now, ans):
        if index >= len(nums):
            return

        value, count = nums[index]
        for j in range(1, count + 1):
            new_ans = now + [value] * j
            ans.append(new_ans)
            self.dfs(index + 1, nums, new_ans, ans)
        self.dfs(index + 1, nums, now, ans)

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums2 = {}
        for value in nums:
            if value not in nums2:
                nums2[value] = 0
            nums2[value] += 1
        listnum = [[k,v]for k,v in nums2.items()]

        ret = [[]]
        self.dfs(0, listnum, [], ret)
        return ret


if __name__ == "__main__":
    s = Solution()
    ret = s.subsetsWithDup([1,2,2])
    print(ret)
