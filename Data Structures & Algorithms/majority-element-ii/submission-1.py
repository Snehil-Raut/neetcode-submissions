from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequencies = Counter(nums)
        li = []
        for k,v in frequencies.items():
            if v > len(nums)//3:
                li.append(k)
        
        return li