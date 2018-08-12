class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        stack = []
        heights.append(0)
        stack.append(heights[0])
        ret_ans = heights[0]
        for i in range(1, len(heights)):
            if heights[i] >= stack[-1]:
                stack.append(heights[i])
            else:
                cnt = 1
                while len(stack) > 0 and heights[i] < stack[-1]:
                    cnt += 1
                    ret_ans = max(ret_ans, stack[-1] * (cnt - 1))
                    stack.pop(-1)
                stack.extend([heights[i]] * cnt )
        return ret_ans



if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))
    print(s.largestRectangleArea([2,1,2]))
