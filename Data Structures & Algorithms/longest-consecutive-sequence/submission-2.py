class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        
        longest = 1
        current = 1
        sort_set = sorted(set(nums))
        
        for i in range(len(sort_set)-1):
            if(sort_set[i+1] == sort_set[i]+1):
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)
        