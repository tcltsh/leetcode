class Solution:
    def findInRow(self, datas, target):
        low = 0
        high = len(datas) - 1
        while low <= high:
            mid = (low + high) // 2
            if datas[mid] == target:
                return True
            elif datas[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        for i in range(1, len(matrix)):
            if matrix[i][0] > target:
                return self.findInRow(matrix[i-1], target)

        return self.findInRow(matrix[-1], target)

if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix([[1]], 1))
