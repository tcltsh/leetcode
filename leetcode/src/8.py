class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        mul = 1
        ret = 0
        while len(str) > 0 and str[0] == ' ':
            str = str[1:]
        if len(str) > 0 and str[0] in ['+', '-']:
            if str[0] == '-':
                mul = -1
            str = str[1:]
        while len(str) > 0 and str[0] == '0':
            str = str[1:]
        for c in str:
            if ord(c) not in range(ord('0'), ord('9') + 1):
                break
            ret = ret * 10 + ord(c) - ord('0')
        ret *= mul
        if ret >= 2 ** 31:
            ret = 2 ** 31 - 1
        if ret <= -2 ** 31:
            ret = -2 ** 31
        return ret

if __name__ == "__main__":
    s = Solution()
    print s.myAtoi("+123")
    print s.myAtoi("-123")
    print s.myAtoi("+0001234")
    print s.myAtoi("0012")
    print s.myAtoi("-001235")
    print s.myAtoi("0000")
    print s.myAtoi("-0000")
    print s.myAtoi("0")
    print s.myAtoi("")
    print s.myAtoi("abc")
    print s.myAtoi("+abc")
    print s.myAtoi("+123ab")
    print s.myAtoi("+123ab")
    print s.myAtoi("+00ab123ab")
    print s.myAtoi("-  00124")
    print s.myAtoi("+  0012   4")
    print s.myAtoi("   +  0012   4")
