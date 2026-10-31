class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        left=0
        max_len=0

        for right in range(len(s)):
            
            if(s[right] not in result):
                result.add(s[right])
                
            else:
                while (s[right]) in result:
                    result.remove(s[left])
                    left+=1
                result.add(s[right])
                
                
            window = (right-left)+1
            max_len=max(max_len,window)
            
            
        return max_len       
                



        