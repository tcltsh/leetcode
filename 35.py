class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        if target > nums[-1]:
            return len(nums)

        if target < nums[0]:
            return 0

        low = 0
        high = len(nums) - 1
        while low + 1 < high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid
            else:
                low = mid
        if nums[low] == target:
            return low
        elif nums[high] == target:
            return high
        return low + 1

if __name__ == '__main__':
    s = Solution()
    print s.searchInsert([1,3,5,6], 5)
    print s.searchInsert([1,3,5,6], 2)
    print s.searchInsert([1,3,5,6], 7)
    print s.searchInsert([1,3,5,6], 0)
