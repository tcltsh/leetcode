import copy

class Solution(object):
    def update(self, ans, x, y, total, target):
        cnt = 1
        for i in range(x+1, total):
            ans[i][y] = target
            if x + cnt < total and y + cnt < total:
                ans[x + cnt][y + cnt] = 'R'
            if x - cnt >= 0 and y - cnt >= 0:
                ans[x - cnt][y - cnt] = 'R'

    def dfs(self, now, total, nowans):
        if now == total:
            ans = copy.deepcopy(nowans)
            pushans = []
            for line in ans:
                for row in range(0, len(line)):
                    if line[row] == "R":
                        line[row] = "."
                pushans.append("".join(line[row]))
            self.ans.append(pushans)

        for i in range(0, total):
            if nowans[now][i] == ".":
                self.update(nowans, now, i, total)
                self.dfs(now + 1, total, nowans)
                self.reback(nowans, now, i, total)
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.ans = []
        self.dfs(0, n, [["." for col in range(n)] for row in range(n)])

if __name__ == "__main__":
    s = Solution()
    print s.solveNQueens(3)
