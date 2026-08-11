class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        left=0
        right=0
        max_len=0

        while right < len(s):
            dic[s[right]] = dic.get(s[right],0)+1

            max_freq = max(dic.values())

            while (right-left+1) - max_freq > k:
                dic[s[left]] -= 1
                left+=1

            window = right-left+1
            max_len = max(window,max_len)
            right+=1
        return max_len


            
        