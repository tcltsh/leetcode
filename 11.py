'''
贪心:从两头开始遍历，假设目前遍历到left,right.因为长度是在不断缩小的，所以如果下一次想要变得更大，只能改变left,right之前短的那条边，长的改了没用
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        left = 0
        right = len(height) - 1
        while left < right:
            ret = max(ret, (right - left) * min(height[right], height[left]))
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return ret

if __name__ == "__main__":
    s = Solution()
    print s.maxArea([1, 2, 1])
