class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low,high=0,len(matrix)*len(matrix[0])-1
        while low<=high:
            mid=(low+high)//2
            r,c=mid//len(matrix[0]),mid%len(matrix[0])
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                low+=1
            else:
                high-=1
        return False
