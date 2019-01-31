class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        dp = [0] * (len(s) + 2)
        dp[len(s)] = 1
        dp[len(s) - 1] = 0 if s[-1] == "0" else 1
        for index in range(len(s) - 2, -1, -1):
            if s[index] == "1":
                dp[index] = dp[index+1] + dp[index+2]
            elif s[index] == "2" and s[index + 1] in ("0", "1", "2", "3", "4", "5", "6"):
                dp[index] = dp[index+1] + dp[index+2]
            elif s[index] == "0":
                dp[index] = 0
            else:
                dp[index] = dp[index + 1]
        return dp[0]

if __name__ == "__main__":
    s = Solution()
    ret = s.numDecodings("2")
    print(ret)

