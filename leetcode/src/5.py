class Solution(object):

    def judge(self, idx, step, s):
        front = idx + step
        tail = idx
        find = False
        ret = ""
        while True:
            if front >= len(s)      \
                or tail < 0         \
                or s[front] != s[tail]:
                break
            find = True
            front += 1
            tail -= 1
        if (front - 1) < len(s) and (tail + 1) >= 0 and find is True:
            ret = s[tail+1: front]
        return ret

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        retstr = ""
        for i in range(0, len(s)):
            for j in range(0, 2):
                now = self.judge(i, j, s)
                if len(now) > len(retstr):
                    retstr = now
        return retstr

if __name__ == "__main__":
    s = Solution()
    print s.longestPalindrome("bbbb")
    print s.longestPalindrome("cbbd")
