class Solution(object):
    def search(self, nums, add, target):
        low = 0
        high = len(nums) - 1
        while (low + 1 < high):
            mid = (low + high) / 2
            if nums[mid] == target:
                if add == 0:
                    high = mid
                else:
                    low = mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if nums[low] == target and nums[high] == target:
            if add == 0:
                return low
            else:
                return high
        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        return -1


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        left = self.search(nums, 0, target)
        if left == -1:
            return [-1, -1]

        right = self.search(nums, 1, target)
        if right == -1:
            return [-1, -1]
        return [left, right]

if __name__ == '__main__':
    s = Solution()
    print s.searchRange([5, 7, 7, 8, 8, 10], 8)
    print s.searchRange([5, 7, 7, 8, 8, 8, 10], 8)
    print s.searchRange([5, 7, 7, 8, 8, 10], 10)
    print s.searchRange([5, 7, 7, 8, 8, 10], 1)
