#!/usr/bin/env python
# coding=utf-8
# @Time    : 2018/4/4 19:33
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 64.py
# @Desc    :

class Solution(object):
    def minPathSum(self, grid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m = len(grid)
        if m <= 0:
            return 0
        n = len(grid[0])

        dp = []
        for i in range(0, m):
            dp.append([])
            for j in range(0, n):
                dp[i].append(grid[i][j])
                if i > 0 and j > 0 :
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])
                elif i > 0:
                    dp[i][j] += dp[i-1][j]
                elif j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]



if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]))