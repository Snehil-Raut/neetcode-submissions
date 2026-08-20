class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        opstr = ""
        min_len = len(min(strs))

        if len(strs) == 0:
            return ""

        for col in range(0,min_len):
            ref_str = strs[0][col]
            for row in range(1,len(strs)):
                if strs[row][col] != ref_str:
                    return opstr
            opstr += ref_str
        
        return opstr
        