class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""

        ans = [1]
        for s in range(0, n-1):
            print s
            newans = []
            cnt = 0
            last = -1
            for i in range(0, len(ans)):
                if ans[i] == last:
                    cnt += 1
                else:
                    if last > 0:
                        newans.append(cnt)
                        newans.append(last)
                    cnt = 1
                    last = ans[i]
            if last > 0:
                newans.append(cnt)
                newans.append(last)
            ans = newans

        ret = ""
        for i in range(0, len(ans)):
            ret += chr(ord('0') + ans[i])
        return ret

if __name__ == "__main__":
    s = Solution()
    print s.countAndSay(1)
    print s.countAndSay(2)
    print s.countAndSay(3)
    print s.countAndSay(4)
