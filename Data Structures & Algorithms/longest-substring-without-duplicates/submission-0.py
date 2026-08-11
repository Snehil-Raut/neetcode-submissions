class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chrset = set()
        res = 0
        left = 0
        for right in range(len(s)):
            while s[right] in chrset:
                chrset.remove(s[left])
                left+=1
            chrset.add(s[right])
            res = max(res, right-left+1)
        return res

        