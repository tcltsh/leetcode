#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 12:30
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 53.py
# @Desc    :

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        now = nums[0]
        for i in range(1, len(nums)):
            now = now + nums[i]
            if now < nums[i]:
                now = nums[i]
            ret = max(ret, now)
        return ret
