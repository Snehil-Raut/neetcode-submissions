
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        left=0
        right=0

        s1_dict = {}
        for x in s1:
            s1_dict[x] = s1_dict.get(x, 0) + 1
        
        s2_dict = {}

        while right < len(s2):
            
            s2_dict[s2[right]] = s2_dict.get(s2[right], 0) + 1

            window_size = right - left + 1 

            if window_size == k:
                if s1_dict == s2_dict:
                    return True
                
                s2_dict[s2[left]] -= 1

                if s2_dict[s2[left]] == 0:
                    s2_dict.pop(s2[left], None)

                left+= 1
                
            right+=1
        
        return False

