class Solution(object):
    ROMA = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    ROMA_TO_INT = [1, 5, 10, 50, 100, 500, 1000]
    def add(self, c, next):
        if next == '0' or self.ROMA.index(c) >= self.ROMA.index(next):
            ind = self.ROMA.index(c)
            return self.ROMA_TO_INT[ind]
        else:
            ind = self.ROMA.index(c)
            return -self.ROMA_TO_INT[ind]

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        s += '0'
        for i in range(0, len(s) - 1):
            ret += self.add(s[i], s[i + 1])
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.romanToInt('MCMLXXX')