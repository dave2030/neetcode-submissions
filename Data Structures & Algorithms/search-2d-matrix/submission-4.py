class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        high=len(matrix[0]) * len(matrix) - 1
        while low<=high:
            mid = low + (high-low)//2
            row = mid//len(matrix[0])
            col = mid %len(matrix[0])
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                low=mid+1
            else:
                high=mid-1
        return False