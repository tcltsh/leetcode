class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        ret = ""
        i = 0
        while True:
            c = None
            for s in strs:
                if len(s) <= i:
                    return ret
                if c is None:
                    c = s[i]
                else:
                    if c != s[i]:
                        return ret
            ret += c
            i += 1
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.longestCommonPrefix(["aabad", "agaba"])
