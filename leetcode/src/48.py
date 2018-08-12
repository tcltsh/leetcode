class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        totaln = len(matrix)
        nown = totaln
        now0 = 0
        nowmax = totaln
        while nown > 1:
            for i in range(0, nowmax - now0 - 1):
                matrix[i + now0][now0], matrix[now0][nowmax - i - 1], matrix[nowmax - i - 1][nowmax - 1], matrix[nowmax-1][i + now0]      \
                        = matrix[nowmax-1][i + now0], matrix[i + now0][now0], matrix[now0][nowmax - i - 1], matrix[nowmax - i - 1][nowmax - 1],
            nown -= 2
            now0 += 1
            nowmax -=1

if __name__ == "__main__":
    s = Solution()
    mat = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
    ]
    s.rotate(mat)
    print mat
