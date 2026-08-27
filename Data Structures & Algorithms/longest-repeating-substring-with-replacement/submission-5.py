class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        max_len = 0
        left=0
        right=0

        while right < len(s):
            dic[s[right]] = dic.get(s[right],0) + 1

            window_size = right - left + 1

            replace_count = window_size - max(dic.values())

            if (replace_count <= k):

                max_len = max(window_size, max_len)
                right+=1
            
            else:
                dic[s[left]] -= 1
                left += 1
                right+=1
        
        return max_len




        


            
        