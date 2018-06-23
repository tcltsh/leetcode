import math, cmath

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = math.sqrt(x)
        return int(r)


if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(8))
    print(s.mySqrt(4))
    print(s.mySqrt(15))
