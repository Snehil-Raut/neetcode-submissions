class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if(len(strs)==0):
            return strs
        
        results = {}

        for x in strs:
            sorted_x = "".join(sorted(x))
            results.setdefault(sorted_x,[]).append(x)

        
        values = list(results.values())
        return values