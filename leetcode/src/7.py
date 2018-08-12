class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        md = x
        mul = 1
        if x < 0:
            mul = -1
            md = -x
        ret = 0
        while md > 0:
            now = md % 10
            ret = ret * 10 + now
            md /= 10
        ret *= mul
        if ret >= 2**31 or ret <= -2 **31:
            return 0
        return ret

if __name__ == "__main__":
    s = Solution()
    print s.reverse(123)
    print s.reverse(-123)
    print s.reverse(1534236469)
