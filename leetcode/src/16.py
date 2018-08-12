class Solution(object):
    def ksum_closest(self, nums, k, target):
        ret = None
        if len(nums) < k:
            return None
        if k == 2:
            begin = 0
            end = len(nums) - 1
            ret = nums[begin] + nums[end]
            while begin < end:
                if abs(nums[begin] + nums[end] - target) < abs(ret - target):
                    ret = nums[begin] + nums[end]
                newabs1 = abs(nums[begin + 1] + nums[end] - target)
                newabs2 = abs(nums[begin] + nums[end - 1] - target)
                if newabs1 < abs(ret - target):
                    begin += 1
                else:
                    end -= 1
        else:
            for i in range(0, len(nums)):
                last = self.ksum_closest(nums[i+1:], k-1, target - nums[i])
                if last is None:
                    continue

                if ret is None:
                    ret = last + nums[i]
                    continue

                if abs(last + nums[i] - target) < abs(ret - target):
                    ret = last + nums[i]
                    #print 'last %d nums:%d update:%d' % (last, nums[i], ret)
                if ret == target:
                    return ret
        return ret
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.ksum_closest(sorted(nums), 3, target)

if __name__ == '__main__':
    s = Solution()
    print s.threeSumClosest([-1, 2, 1, -4], 1)
    print s.threeSumClosest([0,5,-1,-2,4,-1,0,-3,4,-5], 1)
    print s.threeSumClosest([-1,0,1,1,55], 3)
