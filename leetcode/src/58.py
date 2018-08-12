#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 19:49
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 58.py
# @Desc    :

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        s = s.strip()
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                break
            ret += 1
        return ret
