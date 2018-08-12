class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        record = [0] * len(s)
        ret = 0
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    continue
                idx = stack.pop()
                now = i - idx + 1
                pre = 0
                if idx > 0:
                    pre = record[idx - 1]
                ret = max(ret, now + pre)
                record[i] = now + pre
        return ret
