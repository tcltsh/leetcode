#!/usr/bin/env python
# coding=utf-8
# @Time    : 2018/4/4 19:19
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 62.py
# @Desc    :

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = []
        for i in range(0, m):
            dp.append([])
            for j in range(0, n):
                dp[i].append(0)
                dp[0][0] = 1
                if i > 0 :
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]



if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))
