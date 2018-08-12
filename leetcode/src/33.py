class Solution(object):
    def doSearch(self, nums, begin, end, target):
        while begin + 1 < end:
            mid = (begin + end) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                begin = mid
            else:
                end = mid
        if nums[begin] == target:
            return begin
        elif nums[end] == target:
            return end
        else:
            return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        begin = 0
        end = len(nums) - 1
        while begin < end - 1:
            mid = (begin + end) // 2
            if nums[mid] < nums[begin]:
                end = mid
            else:
                begin = mid
        if nums[begin] < nums[end]:
            begin = end

        if target >= nums[0] and target <= nums[begin]:
            return self.doSearch(nums, 0, begin, target)
        if begin + 1 < len(nums) and target <= nums[-1] and target >= nums[begin + 1]:
            return self.doSearch(nums, begin+1, len(nums) - 1, target)
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.search([9, 1, 2, 3], 3)
    print s.search([9, 1, 2, 3], 9)
    print s.search([9, 1, 2, 3], -1)
    print s.search([1, 2, 4, 8], 3)
