
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ret = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[ret] = nums[i]
                ret += 1
        return ret
