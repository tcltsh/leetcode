class Solution(object):
    def update(self, x, y, c):
        k = ord(c) - ord('0') - 1
        od = 1 << k
        self.mapper[0][x] = self.mapper[0][x] | od
        self.mapper[1][y] = self.mapper[1][y] | od
        num = x // 3 * 3 + y // 3
        self.mapper[2][num] = self.mapper[2][num] | od

    def remove(self, x, y, c):
        k = ord(c) - ord('0') - 1
        od = 1 << k
        self.mapper[0][x] = self.mapper[0][x] ^ od
        self.mapper[1][y] = self.mapper[1][y] ^ od
        num = x // 3 * 3 + y // 3
        self.mapper[2][num] = self.mapper[2][num] ^ od

    def calc(self, x, y):
        num = x // 3 * 3 + y // 3
        left = self.mapper[0][x] |self.mapper[1][y] | self.mapper[2][num]
        ret = []
        for i in range(0, 9):
            if left % 2 == 0:
                ret.append(chr(ord('0') + i + 1))
            left = left >> 1
        return ret

    def printM(self):
        for t in self.mapper:
            now = []
            for k in t:
                nowst = ''
                kk = k
                for i in range(0,9):
                    nowst += str(kk %2)
                    kk >>= 1
                now.append(nowst)
            print now
        print '---'

    def dfs(self, point, board):
        if len(point) == 0:
            return True

        now = point.pop()
        nowx = now[0]
        nowy = now[1]
        st = self.calc(nowx, nowy)
        if len(st) == 0:
            point.append(now)
            return False

        for s in st:
            board[nowx][nowy] = s
            self.update(nowx, nowy, s)
            ret = self.dfs(point, board)
            if ret == True:
                return ret
            self.remove(nowx, nowy, s)

        board[nowx][nowy] = '.'
        point.append([nowx, nowy])
        return False


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        self.mapper = [[0] * 9, [0] * 9, [0] * 9]
        point = []
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    point.append([i, j])
                else:
                    self.update(i, j, board[i][j])
        self.dfs(point, board)

def changeStrList(strlist):
    ret = []
    for str in strlist:
        now = []
        for c in str:
            now.append(c)
        ret.append(now)
    return ret

if __name__ == "__main__":
    s = Solution()
    strlist = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]

    add = changeStrList(strlist)
    s.solveSudoku(add)
    print add
