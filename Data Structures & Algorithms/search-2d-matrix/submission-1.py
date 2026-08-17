class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_matrix = []

        for mat in matrix:
            for m in mat:
                flat_matrix.append(m)
        
        left=0
        right= len(flat_matrix)-1
        while left <= right:
            mid = (left+right)//2
            if(flat_matrix[mid]==target):
                return True
            elif (flat_matrix[mid] > target):
                right=mid-1
            elif(flat_matrix[mid] < target):
                left=mid+1
        else:
            return False
        