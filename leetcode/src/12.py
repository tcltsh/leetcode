class Solution(object):
    def plus(self, k, upbase, base, add):
        ret = ""
        if k == 9:
            ret = add + upbase
        elif k >= 5 and k < 9:
            ret = base
            ret += (k-5) * add
        elif k == 4:
            ret = add + base
        else:
            ret = k * add
        return ret

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ""
        if num >= 1000:
            ret += self.plus(num/1000, 'NO', 'NO', 'M')
            num = num % 1000
        if num >= 100:
            ret += self.plus(num/100, 'M', 'D', 'C')
            num = num % 100
        if num >= 10:
            ret += self.plus(num/10, 'C', 'L', 'X')
            num = num % 10
        if num > 0:
            ret += self.plus(num, 'X', 'V', 'I')
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.intToRoman(46)
    print s.intToRoman(47)
    print s.intToRoman(36)
    print s.intToRoman(34)
