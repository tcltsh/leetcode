class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(0, len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                nums[ret] = nums[i]
                ret += 1
        return ret
