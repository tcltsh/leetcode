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
                if i + 1 < len(nums) and flag - nums[i] < nums[i + 1]:
                    break
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                now = self.ksum(nums, i + 1, k-1, flag - nums[i])
                for ans in now:
                    newans = [nums[i]]
                    newans.extend(ans)
                    ret.append(newans)
        return ret


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.ksum(sorted(nums), 0, 3, 0)


if __name__ == '__main__':
    s = Solution()
    print s.threeSum([0,0,0])
    print s.threeSum([-1, 2, 3, 4, 0, 9, 8, -1])
    print s.threeSum([-1, 0, 1, 2, -1, -4])
    print s.threeSum([-2,0,1,1,2])
    print s.threeSum([0,7,-4,-7,0,14,-6,-4,-12,11,4,9,7,4,-10,8,10,5,4,14,6,0,-9,5,6,6,-11,1,-8,-1,2,-1,13,5,-1,-2,4,9,9,-1,-3,-1,-7,11,10,-2,-4,5,10,-15,-4,-6,-8,2,14,13,-7,11,-9,-8,-13,0,-1,-15,-10,13,-2,1,-1,-15,7,3,-9,7,-1,-14,-10,2,6,8,-6,-12,-13,1,-3,8,-9,-2,4,-2,-3,6,5,11,6,11,10,12,-11,-14])
