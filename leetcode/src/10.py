class Solution(object):
    def judge(self, c, p):
        if c == p[0] or p[0] == '.':
            return True

    def dfs(self, s, p, si, pi):
        if pi == len(p) and si == len(s):
            return True

        if pi == len(p) or si == len(s):
            return False

        if p[pi][1] == 0:
            if self.judge(s[si], p[pi]):
                return self.dfs(s, p, si+1, pi+1)
            return False
        else:
            if self.dfs(s,p,si, pi+1):
                return True
            times = 1
            while si+times-1 < len(s) and self.judge(s[si + times - 1], p[pi]):
                if self.dfs(s, p, si + times, pi + 1):
                    return True
                times += 1
        return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s += "$"
        p += "$"
        pi = 0
        newp = []
        for i in range(0, len(p)):
            if p[i] == "*":
                continue
            if i + 1 < len(p) and p[i + 1] == "*":
                newp.append([p[i], 1])
            else:
                newp.append([p[i], 0])

        return self.dfs(s, newp, 0, 0)

if __name__ == "__main__":
    s = Solution()
    print s.isMatch("aa", "a")
    print s.isMatch("aa", "aa")
    print s.isMatch("aaa", "aa")
    print s.isMatch("aa", "a*")
    print s.isMatch("aa", ".*")
    print s.isMatch("ab", ".*")
    print s.isMatch("aab", "c*a*b")
    print s.isMatch("ab", ".*c")
    print s.isMatch("a", "ab*")
