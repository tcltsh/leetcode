class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(0, l):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]

if __name__ == "__main__":
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 9);
