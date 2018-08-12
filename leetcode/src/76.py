class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) == 0:
            return ""

        cnt = {}
        should = {}
        for i in t:
            if i not in cnt:
                cnt[i] = 0
                should[i] = 0
            should[i] += 1
        total_match = 0

        min_cnt = len(s) + 1
        start = 0
        ans_start = -1

        for i in range(0, len(s)):
            if s[i] in cnt:
                if cnt[s[i]] < should[s[i]]:
                    total_match += 1
                cnt[s[i]] += 1

            while start < i:
                if s[start] not in cnt:
                    start += 1
                    continue
                if cnt[s[start]] <= should[s[start]]:
                    break
                cnt[s[start]] -= 1
                start += 1
            if total_match == len(t):
                now_cnt = i - start + 1
                if now_cnt < min_cnt:
                    min_cnt = now_cnt
                    ans_start = start

        if ans_start < 0:
            return ""
        return s[ans_start: ans_start + min_cnt]

if __name__ =="__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("acbbaca", "aba"))
