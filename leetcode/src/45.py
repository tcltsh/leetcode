#encoding:utf-8

class Solution(object):
    def jumpDp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [len(nums)] * len(nums)
        minidx = [-1] * len(nums)
        dp[0] = 0
        for i in range(0, len(nums)):
            last = minidx[i]
            begin = 0
            if last >= 0:
                begin = nums[last] + last - i
            for j in range(max(begin + 1, 1), nums[i] + 1):
                if i + j < len(nums) and dp[i + j] > dp[i] + 1:
                    dp[i + j] = dp[i] + 1
                    minidx[i + j] = i
        return dp[len(nums) - 1]

    def jump(self, nums):
        fur = 0
        cur = 0
        curEnd = 0
        jumps = 0
        while cur < len(nums) - 1:
            fur = max(fur, cur + nums[cur])
            if cur == curEnd:
                jumps += 1
                curEnd = fur
            cur += 1
        return jumps

if __name__ == "__main__":
    s = Solution()
    print s.jump([2,3,1,1,4])
    print s.jump([1, 2, 3])
    print s.jump([1,1,1,1])
