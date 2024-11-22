class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp_arr = [row[:] for row in matrix]
        
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix):
                matrix[j][abs(len(matrix)-i-1)] = temp_arr[i][j]
                j += 1
            i += 1