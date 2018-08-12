import copy

class Solution:
    def dfs(self, board, word, flag, now, x, y):
        if now == len(word):
            return True
        stepx = [-1, 1, 0, 0]
        stepy = [0, 0, 1, -1]

        for i in range(0, len(stepx)):
            xa = stepx[i]
            ya = stepy[i]
            newx = x + xa
            newy = y + ya
            if newx < 0 or newy < 0:
                continue
            if newx >= len(board) or newy >= len(board[newx]):
                continue
            if board[newx][newy] != word[now]:
                continue
            if flag[newx][newy] == True:
                continue
            flag[newx][newy] = True
            ret = self.dfs(board, word, flag, now+1, newx, newy)
            if ret == True:
                return ret
            flag[newx][newy] = False
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0:
            return False

        flag = []
        cnt = 0
        for i in range(0, len(board)):
            flag.append([])
            for j in range(0, len(board[i])):
                flag[i].append(False)
                cnt += 1


        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == word[0]:
                    flag[i][j] = True
                    if self.dfs(board, word, flag, 1, i, j):
                        return True
                    flag[i][j] = False
        return False

if __name__ == "__main__":
    s = Solution()
