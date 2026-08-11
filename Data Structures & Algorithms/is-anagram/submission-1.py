class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        x = "".join(sorted(s))
        y = "".join(sorted(t))

        return x==y
        