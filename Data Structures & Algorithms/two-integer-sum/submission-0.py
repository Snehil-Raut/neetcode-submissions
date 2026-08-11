class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}
        li = []
        for i,x in enumerate(nums):
            is_seen = target - x
            if(is_seen not in results):
                results[x] = i
            else:
                li.append(results[is_seen])
                li.append(i)
        
        return li

        
