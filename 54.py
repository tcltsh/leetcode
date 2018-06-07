#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 12:36
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 54.py
# @Desc    :

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 0:
            return []
        ret = []
        line_begin = 0
        line_end = len(matrix[0])
        row_begin = 0
        row_end = len(matrix)
        while True:
            if line_begin >= line_end - 1 or row_begin >= row_end - 1:
                break
            for i in range(line_begin, line_end - 1):
                ret.append(matrix[row_begin][i])
            for i in range(row_begin, row_end - 1):
                    ret.append(matrix[i][line_end - 1])
            for i in range(line_end - 1, line_begin, -1):
                    ret.append(matrix[row_end - 1][i])
            for i in range(row_end - 1, row_begin, -1):
                ret.append(matrix[i][line_begin])

            line_begin += 1
            row_begin += 1
            line_end -= 1
            row_end -= 1
        if line_begin == line_end - 1 and row_begin == row_end - 1:
            ret.append(matrix[row_begin][line_begin])
        elif line_begin == line_end - 1 and row_begin < row_end - 1:
            for i in range(row_begin, row_end):
                ret.append(matrix[i][line_begin])
        elif row_begin == row_end - 1 and line_begin < line_end - 1:
            for i in range(line_begin, line_end):
                ret.append(matrix[row_begin][i])
        return ret


if  __name__ == "__main__":
    s = Solution()
    print s.spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    print s.spiralOrder([[6,9,7]])
