import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        low = 1
        high = max(piles)

        min_bananas_toeat = []
        while low <= high:
            mid = (low + high) // 2
            eat_rate = []
            for pile in piles:
                eat_rate.append(math.ceil(pile / mid))
            
            if sum(eat_rate) <= h:
                min_bananas_toeat.append(mid)
                high=mid-1

                eat_rate.clear()
            
            elif(sum(eat_rate) > h):
                low = mid + 1
            

        return min(min_bananas_toeat)





        

        