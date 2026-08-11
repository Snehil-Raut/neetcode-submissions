class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}

        for x in nums:
            if x not in result:
                result[x] = 1
            else:
                result[x] += 1
        
        sorted_values = dict(sorted(result.items(),key=lambda x: x[1], reverse=True))
        
        top_k_values = list(sorted_values.keys())

        return top_k_values[:k]
        




            
            

        
        
        