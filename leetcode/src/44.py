#encoding:utf-8
import re

'''
dp的时间复杂度为O(nm),n,m分别为两个str的长度
这里有一种贪心法：
注意*的特性，只要能在贪心到下一个*，那么一切可以从头开始算。所以每次贪心只需要记录上一个*的位置，以及上一个*代表了几个字符。如果遇到了*，则可以从当前重新贪心
'''

class Solution(object):
    def isMatchDp(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        newp = ""
        for i in range(0, len(p)):
            if p[i] != "*":
                newp += p[i]
            else:
                if i == 0 or p[i - 1] != "*":
                    newp += p[i]
        dp = [[ False ] * (len(s) + 1 ) for i in range(0, len(newp) + 1)]
        dp[0][0] = True

        stack = [[0, 0]]
        while stack:
            now = stack.pop(0)
            i = now[0]
            j = now[1]
            if i < len(newp) and j < len(s) and (newp[i] == s[j] or newp[i] == "?"):
                if dp[i+1][j+1] == False:
                    dp[i+1][j+1] = True
                    stack.append([i+1, j+1])
            if i < len(newp) and newp[i] == "*":
                for k in range(j, len(s) + 1):
                    if dp[i+1][k] == False:
                        dp[i+1][k] = True
                        stack.append([i+1, k])
            if dp[len(newp)][len(s)] == True:
                return True
        return False

    def isMatch(self, s, p):
        cur_s = 0
        cur_p = 0
        star = -1
        recordp = -1

        while cur_s < len(s):
            if cur_s < len(s) and cur_p < len(p) and (s[cur_s] == p[cur_p] or p[cur_p] == "?"):
                cur_s += 1
                cur_p += 1
            elif cur_p < len(p) and p[cur_p] == "*":
                star = cur_p
                match = cur_s
                cur_p += 1
                recordp = cur_p
            elif star >= 0:
                cur_s = match + 1
                cur_p = recordp
                match += 1
            else:
                return False
        while cur_p < len(p) and p[cur_p] == "*":
            cur_p += 1
        return cur_p == len(p) and cur_s == len(s)

if __name__ == "__main__":
    s = Solution()
    print s.isMatch("bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa",
                    "******a?a*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****")
    print s.isMatch("", "*")
    print s.isMatch("aa", "*")
