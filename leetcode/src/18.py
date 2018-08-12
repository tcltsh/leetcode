class Solution(object):
    def ksum(self, nums, begin, k, flag):
        # print nums, k, flag
        ret = []
        if k + begin > len(nums):
            return ret
        if k == 2:
            head = begin
            tail = len(nums) - 1
            while head < tail:
                now = nums[head] + nums[tail]
                if now == flag:
                    ret.append([nums[head], nums[tail]])
                    tail -= 1
                    head += 1
                    while tail > head and nums[tail] == nums[tail+1]:
                        tail -= 1
                    while head < tail and nums[head] == nums[head-1]:
                        head += 1
                elif now > flag:
                    tail -= 1
                else:
                    head += 1
        else:
            for i in range(begin, len(nums)):
                if i > begin and nums[i] == nums[i-1]:
                    continue
                now = self.ksum(nums, i + 1, k-1, flag - nums[i])
                for ans in now:
                    newans = [nums[i]]
                    newans.extend(ans)
                    ret.append(newans)
        return ret


    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.ksum(sorted(nums), 0, 4, target)


if __name__ == '__main__':
    s = Solution()
    #print s.fourSum([1, 0, -1, 0, -2, 2], 0)
    #print s.fourSum([0,0,0,0], 0)
    print s.fourSum([1,-2,-5,-4,-3,3,3,5], -11)
