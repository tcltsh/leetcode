class Solution:
    def dfs(self, s1, s2):
        if s1 == s2:
            return True

        ss1 = "".join((lambda x:(x.sort(),x)[1])(list(s1)))
        ss2 = "".join((lambda x:(x.sort(),x)[1])(list(s2)))
        if ss1 != ss2:
            return False

        for i in range(1, len(s1)):
            s1_pre = s1[0:i]
            s1_end = s1[i:]
            s2_pre = s2[0: len(s2) - i]
            s2_end = s2[len(s2) - i:]
            if self.dfs(s1_pre, s2_end) and self.dfs(s1_end, s2_pre):
                return True
            if self.dfs(s1[0:i], s2[0:i]) and self.dfs(s1[i:], s2[i:]):
                return True
        return False

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return self.dfs(s1, s2)

if __name__ == "__main__":
    s = Solution()
    res = s.isScramble("abcd", "dacb")
    print(res)
