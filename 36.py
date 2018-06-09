class Solution(object):
    def judge(self, arr):
        if len(arr) != 9:
            return False
        fd = []
        for c in arr:
            if c == '.':
                continue
            if c in fd:
                return False
            fd.append(c)
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != 9:
            return False
        for s in board:
            if len(s) != 9:
                return False
            if self.judge(s) == False:
                return False

        for i in range(0, 9):
            arr = []
            for j in range(0, 9):
                arr.append(board[j][i])
            if self.judge(arr) == False:
                return False

        for i in range(0, 3):
            for j in range(0, 3):
                arr = []
                for k in range(0, 3):
                    for l in range(0, 3):
                        arr.append(board[i * 3 + k][j * 3 + l])
                if self.judge(arr) == False:
                    return False
        return True

