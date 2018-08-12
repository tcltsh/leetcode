#!/usr/bin/env python
# coding=utf-8
# @Time    : 2018/4/4 19:38
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 65.py
# @Desc    :


class Solution(object):

    def checkNum(self, s, dot = True):
        if len(s) == 0:
            return False
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        if len(s) == 0:
            return False
        dcnt = 0
        for i in s:
            if ord(i) < ord('0') or ord(i) > ord('9'):
                if dot == False:
                    return False
                if dot == True and i != '.':
                    return False
                if dot == True and i == '.':
                    dcnt += 1
        if dcnt > 1:
            return False
        if s == ".":
            return False
        return True

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0 or s == 'e':
            return False
        ecnt = 0
        for i in s:
            if (not (ord(i) >= ord('0') and ord(i) <= ord('9'))) and i != '.' and i != 'e' and i != '-' and i != '+':
                return False
            if i == 'e':
                ecnt += 1
        if ecnt > 1:
            return False
        if ecnt == 0 and self.checkNum(s):
            return True
        if ecnt == 1:
            epos = s.find('e')
            if self.checkNum(s[0: epos]) and self.checkNum(s[epos+1:], False):
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print (s.isNumber("1 a"))
    print (s.isNumber("  0000 "))
    print (s.isNumber("364"))
    print (s.isNumber("3e6"))
    print (s.isNumber(".e6"))
    print (s.isNumber("00000000000e6."))
    print (s.isNumber(".00000000000e6"))
    print (s.isNumber("00000000000.e6"))
    print (s.isNumber("00000.000000.e6"))
    print (s.isNumber("2e0"))
    print (s.isNumber("e9"))

