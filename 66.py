#!/usr/bin/env python
# coding=utf-8
# @Time    : 2018/4/4 20:16
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 66.py
# @Desc    :

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add = 1
        for i in range(len(digits)-1, -1, -1):
            p = digits[i] + add
            digits[i] = p %10
            add = int(p / 10)
        if add == 1:
            digits = [1] + (digits)
        return digits


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([9,9,9]))

