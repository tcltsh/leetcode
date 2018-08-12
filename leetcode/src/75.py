class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lhead = 0
        ltail = len(nums) - 1
        i = 0
        while i <= ltail:
            if nums[i] == 0:
                nums[lhead], nums[i] = nums[i], nums[lhead]
                lhead += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[ltail] = nums[ltail], nums[i]
                ltail -= 1
            else:
                i += 1


if __name__ == "__main__":
    s = Solution()
    arr = [1,2,0]
    s.sortColors(arr)
    print(arr)

