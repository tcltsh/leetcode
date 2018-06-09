import os,sys

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        has = set()
        bp = 0
        nowlen = 0
        ret = 0
        for c in s:
            if c not in has:
                has.add(c)
                nowlen += 1
            else:
                while s[bp] != c:
                    has.remove(s[bp])
                    bp +=1
                    nowlen -= 1
                bp += 1
            if nowlen >= ret:
                ret = nowlen
        if nowlen > ret:
            ret = nowlen
        return ret

if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring("dvdf")
