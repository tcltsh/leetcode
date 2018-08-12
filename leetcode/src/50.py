class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        mul = x
        if n == 0:
            return 1.0;
        elif n < 0:
            mul = 1.0 / x
            n = -n
        ans = 1.0
        while n >= 1:
            if n & 1 == 1:
                ans *= mul
            mul *= mul
            n = n >> 1;
        return ans

if __name__ == "__main__":
    s = Solution()
    print s.myPow(3,4)

