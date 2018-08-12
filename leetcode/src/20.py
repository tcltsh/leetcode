class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ['{', '[', '(']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c == '}' and stack[-1] != '{':
                    return False
                if c == ']' and stack[-1] != '[':
                    return False
                if c == ')' and stack[-1] != '(':
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False

if __name__ == "__main__":
    s = Solution()
    print s.isValid("{{}{}(()")
    print s.isValid("{{}{}(())}")
