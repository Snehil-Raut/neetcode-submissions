class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = {}

        for i in nums:
            hashtable[i] = hashtable.get(i,0)+1
        
        for k,v in hashtable.items():
            if v > len(nums)/2:
                return k

        