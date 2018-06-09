class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = []
        for i in range(0, numRows):
            arr.append([])

        step = 1
        nowRow = 0
        for c in s:
            arr[nowRow].append(c)
            if nowRow == numRows - 1:
                step = -1
            elif nowRow == 0:
                step = 1
            if nowRow + step in range(0, numRows):
                nowRow += step

        ret = ""
        for a in arr:
            ret += "".join(a)
        return ret

if __name__ == "__main__":
    s = Solution()
    print s.convert("PAYPALISHIRING", 3)
    print s.convert("ABC", 1)
    print s.convert("ABC", 2)
