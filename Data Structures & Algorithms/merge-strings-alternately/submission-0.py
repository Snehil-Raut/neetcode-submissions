class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = []
        min_len_str = min(len(word1),len(word2))

        for char1,char2 in zip(word1,word2):
            res.append(char1+char2)
        
        longest_str = max(word1,word2, key=len)

        for i in range(min_len_str, len(longest_str)):
            res.append(longest_str[i])
        
        res = "".join(res)

        return res