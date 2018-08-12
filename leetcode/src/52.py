import copy

class Solution(object):
    def solve(self, total_line, left_line, now, streight, diag_left, diag_right):
        if left_line == 0:
            self.result += 1
            return
        diag_right = diag_right >> 1
        diag_left = (diag_left << 1)  & ((1 << (total_line + 1)) - 1)
        judge = diag_left |diag_right | streight
        for i in range(0, total_line):
            if judge | (1 << i) != judge:
                now[total_line - left_line] = i
                self.solve(total_line, left_line - 1, now, streight|(1 << i), diag_left |(1 << i), diag_right|(1 << i))


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <= 0:
            return 0
        self.result = 0
        self.solve(n, n, [ -1] *n, 0, 0, 0)
        return self.result

if __name__== '__main__':
    s = Solution()
    print s.solveNQueens(10)
