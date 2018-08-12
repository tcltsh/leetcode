class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        image = 10086
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(0, len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = image
                    for k in range(0, len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = image


        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == image:
                    matrix[i][j] = 0



