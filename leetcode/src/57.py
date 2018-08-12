#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 19:21
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 57.py
# @Desc    :

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ret = []
        nowstart = newInterval.start
        nowend = newInterval.end
        over = False
        for now in intervals:
            if now.end < newInterval.start:
                ret.append(now)
                continue
            if now.start > newInterval.end:
                if over is False:
                    ret.append(Interval(nowstart, nowend))
                over = True
                ret.append(now)
                continue
            nowstart = min( now.start, nowstart)
            nowend = max(nowend, now.end)
        if over is False:
            ret.append(Interval(nowstart, nowend))
        return ret
