
from collections import Counter
class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        
        right=0

        while right < len(s2):
            res = s2[right:right+k]

            if Counter(res) == Counter(s1):
                return True
        
            else: 
                right +=1 
        
        return False



