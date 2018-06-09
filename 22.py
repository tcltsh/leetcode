class Solution(object):
    final = []
    flag = set()
    def dfs(self,str, now,left, remain,total, ans):
        if now == total:
            self.final.append(ans)
        else:
            if left > 0:
                self.dfs(str, now + 1, left -1, remain + 1, total, ans + "(")
            if remain > 0:
                self.dfs(str, now + 1, left, remain - 1, total, ans + ")")

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.final = []
        str = "(" * n
        self.dfs(str, 0,n,0,2*n, "")
        return self.final

if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(3)
    print s.generateParenthesis(4)
