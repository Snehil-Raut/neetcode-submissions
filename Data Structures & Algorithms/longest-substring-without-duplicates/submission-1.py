class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left=0
        right=0
        max_len=0

        while right < len(s):

            #charset.add(s[right])
            while s[right] in charset:
                charset.discard(s[left])
                left+=1

            charset.add(s[right])
            curr_len = right-left+1
            max_len = max(curr_len, max_len)
            right+=1
        return max_len


        