class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        cnt = 2
        cnt_value1 = nums[1]
        cnt_value2 = nums[0]
        for i in range(2, len(nums)):
            before1 = nums[i - 1]
            before2 = nums[i - 2]
            if i - 2 == cnt - 1:
                before2 = cnt_value1
            elif i - 2 == cnt - 2:
                before2 = cnt_value2

            if i - 1 == cnt - 1:
                before1 = cnt_value1
            elif i - 1 == cnt - 2:
                before1 = cnt_value2

            if nums[i] == before1 and nums[i] == before2:
                continue
            cnt_value1 = nums[cnt]
            cnt_value2 = nums[cnt - 1]
            nums[cnt] = nums[i]
            cnt += 1

        return cnt


if __name__ =="__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,1]))
