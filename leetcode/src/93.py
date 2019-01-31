class Solution:
    def dfs(self, ips, index, times, now, ans):
        if times == 0:
            final_number = ips[index:]
            if len(final_number) == 0 or (final_number[0] == "0" and len(final_number) > 1):
                return
            if int(final_number) <= 255:
                ans.append('.'.join(now + [final_number]))
            return

        for i in range(1, 4):
            number = ips[index: index + i]
            if len(number) == 0:
                continue
            if int(number) > 255 or (number[0] == "0" and len(number) > 1):
                continue
            self.dfs(ips, index + i, times - 1, now + [number], ans)

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.dfs(s, 0, 3, [], ans)
        return ans

if __name__ == "__main__":
    s = Solution()
    s.restoreIpAddresses("1111")
