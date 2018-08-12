#!/usr/bin/env python
# coding=utf-8
# @Time    : 2018/4/10 16:10
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 67.py
# @Desc    :

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = ""
        add = 0
        lena = len(a) - 1
        lenb = len(b) - 1
        while lena >= 0 or lenb >= 0:
            now = 0
            if lena >= 0 and lenb >= 0:
                now = int(a[lena]) + int(b[lenb]) + add
                lena -= 1
                lenb -= 1
            elif lena >= 0:
                now = int(a[lena]) + add
                lena -= 1
            else:
                now = int(b[lenb]) + add
                lenb -= 1
            ans = str(now%2) + ans
            add = 1 if now >= 2 else 0
        if add > 0:
            ans = str(add) + ans
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11", "111"))
