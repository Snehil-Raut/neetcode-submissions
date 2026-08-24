class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        
        max_len=0
        charset=set()

        for right in range(len(s)):

            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            
            charset.add(s[right])
            
            curr_len = right-left+1

            max_len = max(curr_len,max_len)
        
        return max_len



        