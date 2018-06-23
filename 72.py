class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        short,long = word1, word2
        if len(word1) > len(word2):
            short, long = word2, word1

        ret = 0
        dp0 = [0] * len(long)
        dp1 = [0] * len(long)
        for i in long:
            if long[i] == short[0]:
                dp0[0] = 1
        return ret + len(long) - len(short)
