class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        left=0
        right=len(heights) - 1

        while left < right:
            width = right-left
            min_height = min(heights[left],heights[right])
            current_area = width * min_height
            
            maxarea = max(current_area,maxarea)

            if (heights[left] < heights[right]):
                left+=1
            else:
                right-=1
        
        return maxarea