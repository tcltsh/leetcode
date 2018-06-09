class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0:
            if nums[i] >= nums[i + 1]:
                i -= 1
            else:
                break

        if i >= 0:
            begin = i + 1
            end = len(nums) - 1
            while begin < end:
                nums[begin], nums[end] = nums[end], nums[begin]
                begin += 1
                end -= 1
            for k in range(i+1, len(nums)):
                if nums[k] > nums[i]:
                    nums[i], nums[k] = nums[k], nums[i]
                    break
        elif len(nums) > 0:
            begin = 0
            end = len(nums) - 1
            while begin < end:
                nums[begin], nums[end] = nums[end], nums[begin]
                begin += 1
                end -= 1

if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1]
    s.nextPermutation(nums)
    print nums
