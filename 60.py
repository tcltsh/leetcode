#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 12:31
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 60.py
# @Desc    :

import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k > math.factorial(n) or k <= 0:
            return ""
        number = [ i for i in range(1, n+1) ]
        ret = ""
        total = math.factorial(n)
        while n > 0:
            next_order = total // n
            now_turn_num = k // next_order
            if now_turn_num == 0:
                choose = 1
            elif next_order * now_turn_num == k:
                choose = now_turn_num
                k =  next_order
            else:
                choose = now_turn_num + 1
                k -= now_turn_num * next_order
            ret += str(number[choose - 1])
            del number[choose - 1]
            n -= 1
            total = next_order
        return ret

if __name__ == "__main__":
    s =  Solution()
    print s.getPermutation(3, 2)
    print s.getPermutation(3, 4)

