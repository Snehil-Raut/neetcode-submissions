class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        right=0
    

        while right < len(s2):
            s3 = s2[right:right+len_s1]

            if sorted(s3)==sorted(s1):
                return True
            right+=1
        return False
        