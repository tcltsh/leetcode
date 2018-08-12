#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 12:20
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 59.py
# @Desc    :

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        ret = [[-1] * n for i in range(0, n)]
        left = up = 0
        right = down = n
        k = 1
        while left < right:
            for i in range(left, right - 1):
                ret[up][i] = k
                k += 1
            for i in range(up, down - 1):
                ret[i][right - 1] = k
                k += 1
            for i in range(right - 1, left, -1):
                ret[down - 1][i] = k
                k += 1
            for i in range(down - 1, up, -1):
                ret[i][left] = k
                k += 1
            left += 1
            up += 1
            right -= 1
            down -= 1
        if k == n * n:
            ret[n/2][n/2] = n * n
        return ret

if __name__ == "__main__":
    s = Solution()
    print s.generateMatrix(3)
