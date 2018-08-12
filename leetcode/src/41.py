class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_pos = 0
        for k in nums:
            if k > 0:
                total_pos += 1
        flag = [False] * (total_pos + 1)

        for k in nums:
            if k > 0 and k <= total_pos:
                flag[k-1] = True

        for i in range(0, len(flag)):
            if flag[i] == False:
                return i + 1

