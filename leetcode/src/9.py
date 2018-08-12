class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x % 10 == 0 and x > 0:
            return False
        b = 0
        while b <= x:
            if b == x:
                return True
            md = x % 10
            b = b * 10 + md
            if b == x:
                return True
            x /= 10
        return False

if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome(-1)
    print s.isPalindrome(12412)
    print s.isPalindrome(1234321)
    print s.isPalindrome(12343210)
    print s.isPalindrome(123321)
    print s.isPalindrome(1233211)
    print s.isPalindrome(1)
    print s.isPalindrome(0)
