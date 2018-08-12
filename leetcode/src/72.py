class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        max_value = len(word1) + len(word2)
        dp = [ [max_value for i in range(len(word2) + 2)] for j in range(len(word1) + 2) ]
        for i in range(0, len(word1) + 1):
            dp[i][0] = i
        for i in range(0, len(word2) + 1):
            dp[0][i] = i
        for i in range(0, len(word1)):
            for j in range(0, len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1] + 1, dp[i+1][j] + 1)
                else:
                    dp[i+1][j+1] = min(dp[i][j+1] + 1, dp[i+1][j] + 1, dp[i][j] + 1)

        return dp[len(word1)][len(word2)]


if __name__ == "__main__":
    s = Solution()
    ret = s.minDistance("horse", "ros")
    print(ret)