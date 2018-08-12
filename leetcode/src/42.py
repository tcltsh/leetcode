class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        last = 0
        add = 0
        ans = 0
        for i in range(1, len(height)):
            if height[i] >= height[last]:
                trap = min(height[i], height[last])
                newadd = trap * (i - last - 1) - add
                if newadd > 0:
                    ans += newadd
                last = i
                add = 0
            else:
                add += height[i]

        last = len(height) - 1
        add = 0
        for i in range(len(height) - 2, -1, -1):
            if height[i] > height[last]:
                trap = min(height[i], height[last])
                newadd = trap * (last - i - 1) - add
                if newadd > 0:
                    ans += newadd
                last = i
                add = 0
            else:
                add += height[i]
        return ans

if __name__ == "__main__":
    s = Solution()
    print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print s.trap([0,0,0,0,0])
    print s.trap([0,0,1,1,1,0])
    print s.trap([0,0,1,0,1,0,1,0])
