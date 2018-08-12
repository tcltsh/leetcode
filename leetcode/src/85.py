class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        llen = len(matrix)
        if llen == 0:
            return 0
        rlen = len(matrix[0])
        if rlen == 0:
            return 0

        ret_value = 0

        height = [0] * (rlen + 1)
        for i in range(0, llen):
            stack = []
            matrix[i].append("0")
            for j in range(0, rlen + 1):
                if matrix[i][j] == "0":
                    height[j] = 0
                else:
                    height[j] += 1

                if len(stack) == 0 or height[j] >= stack[-1]:
                    stack.append(height[j])
                else:
                    cnt = 1
                    while len(stack) > 0 and stack[-1] > height[j]:
                        cnt += 1

                        now = (cnt - 1) * stack[-1]
                        ret_value = max(ret_value, now)
                        stack.pop()
                    for _ in range(0, cnt):
                        stack.append(height[j])
        return ret_value

if __name__ == "__main__":
    s = Solution()
    ret = s.maximalRectangle([["0","1"],["0","1"]])
    print(ret)
