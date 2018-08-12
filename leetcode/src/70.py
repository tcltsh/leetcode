class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0,1,2]
        if n < 3:
            return arr[n]
        for i in range(3, n + 1):
            arr.append(arr[-1] + arr[-2])
            arr.pop(0)

        return arr[-1]
