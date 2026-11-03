import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_eating_speed = max(piles)

        low= 1
        high= max(piles)

        list_min_hrs = []
        while low<=high:
            mid = (low+high)//2
           
            min_hrs = 0
            for i in range(len(piles)):
                hrs_taken = math.ceil(piles[i]/mid)

                min_hrs += hrs_taken
            if min_hrs <= h:
                list_min_hrs.append(mid)
                high=mid-1
                
            else:
                low = mid+1
        
        
        return min(list_min_hrs)

            






        

        