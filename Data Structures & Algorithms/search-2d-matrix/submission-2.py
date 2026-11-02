class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        r = len(matrix)    #get row count
        c = len(matrix[0]) # col count
        high = (r*c) - 1 # total val
    
        while low<=high:
            mid = (low+high)//2
            
            # change to matrix 
            row = mid // c  
            col = mid % c
            mat = matrix[row][col]
            
            if (mat == target):
                return True
            elif(mat > target):
                high = mid-1
            elif(mat<target):
                low=mid+1
        
        return False
