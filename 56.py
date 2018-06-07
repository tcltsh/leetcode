#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 18:54
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 56.py
# @Desc    :

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ret = []
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, cmp = lambda x, y: cmp(x.start, y.start))
        left = intervals[0].start
        right = intervals[0].end
        for i in intervals:
            if  i.start <= right:
                right = max(right, i.end)
            else:
                ret.append(Interval(left, right))
                left = i.start
                right = i.end
        ret.append(Interval(left, right))
        return ret

if __name__ == "__main__":
    s = Solution()
    print s.merge([[1,3], [2,6], [8,10], [15,16]])

