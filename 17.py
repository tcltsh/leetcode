class Solution(object):
    MAPPRE = [
        "","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"
    ]

    def dfs(self, digits):
        ret = []
        pre = []
        now = digits[0]
        order = ord(now) - ord('0')
        now = list(self.MAPPRE[order])
        if len(digits) == 1:
            return now
        else:
            pre = self.dfs(digits[1:])
        for c in now:
            for prec in pre:
                ret.append(c + prec)
        return ret

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        for c in digits:
            if c in ['0', '1']:
                return []
        return self.dfs(digits)

if __name__ == '__main__':
    s = Solution()
    print s.letterCombinations("23")
