#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 13:39
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : 55.py
# @Desc    :

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        dist = nums[0]
        for i in xrange(1, len(nums)):
            if i > dist:
                return False
            dist = max(dist, nums[i] + i)
            if dist >= len(nums) - 1:
                return True
