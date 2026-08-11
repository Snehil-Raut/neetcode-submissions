class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        i = 0

        while i<len(heights)-1:

            j = len(heights)-1
            while j>i:

                distance = j-i  # distance b/n index
                min_ht = min(heights[i],heights[j])

                new_area = distance * min_ht
                
                if(new_area > maxarea):
                    maxarea = new_area
                    
                j-=1

            i+=1

        return maxarea