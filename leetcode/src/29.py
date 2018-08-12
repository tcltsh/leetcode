class Solution(object):
    def doit(self, end, sor, cnt = 0):
        pre = None
        mul = sor
        times = 0
        while mul <= end:
            pre = mul
            mul = mul + mul
            if times == 0:
                times = 1
            else:
                times = times + times
        if pre is None:
            return 0
        if pre < -2147483647 or pre > 2147483647:
            if not (pre == 2147483648 and end == 2147483648 and cnt == 1):
                return -1
        left = end - pre
        ret = self.doit(left, sor)
        return ret + times

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1
        if dividend < -2147483648 or dividend > 2147483647:
            return -2147483647
        if divisor < -2147483648 or divisor > 2147483647:
            return -2147483647
        cnt = 0
        flag = 0
        if dividend < 0:
            dividend = -dividend
            cnt +=1
            flag = 1
        if divisor < 0:
            divisor = -divisor
            cnt += 1

        ret = self.doit(dividend, divisor, flag)
        if ret == -1:
            return 2147483647
        else:
            ans = ret
            if cnt == 1:
                ans = -ret
            if ans < -2147483648 or ans > 2147483647:
                return 2147483647
            else:
                return ans

if __name__ == '__main__':
    s = Solution()
    print s.divide(-2147483648, -1)
