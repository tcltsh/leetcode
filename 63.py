#!/usr/bin/env python
# coding=utf-8
# @Time    : 2018/4/4 19:29
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 63.py
# @Desc    :

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m = len(obstacleGrid)
        if m <= 0:
            return 0
        n = len(obstacleGrid[0])

        dp = []
        for i in range(0, m):
            dp.append([])
            for j in range(0, n):
                dp[i].append(0)
                if i == 0 and j == 0:
                    dp[0][0] = 1
                if i > 0 :
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
        return dp[m-1][n-1]



if __name__ == "__main__":
    s = Solution()
    print(s.uniquePathsWithObstacles([
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]))
